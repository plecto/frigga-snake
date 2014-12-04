from frigga_snake import constants
import re


class Names(object):
    def __init__(self, name):
        self.group = name

        push_matcher = constants.PUSH_PATTERN.match(name)

        the_cluster = push_matcher.group(1) if push_matcher else name

        labeled_vars_matcher = constants.LABELED_VARS_PATTERN.match(the_cluster)
        if not labeled_vars_matcher:
            return

        self.group = name
        self.cluster = the_cluster
        sequence_string = push_matcher.group(3) if push_matcher else None
        if sequence_string:
            self.sequence = int(sequence_string)
        else:
            self.sequence = 0

        unlabeled_vars = labeled_vars_matcher.group(1)
        labeled_vars = labeled_vars_matcher.group(2)

        name_matcher = constants.NAME_PATTERN.match(unlabeled_vars)
        self.app = name_matcher.group(1)
        self.stack = name_matcher.group(2)
        self.detail = name_matcher.group(3)

        self.countries = self._extract_labeled_variable(labeled_vars, constants.COUNTRIES_KEY)
        self.dev_phase = self._extract_labeled_variable(labeled_vars, constants.DEV_PHASE_KEY)
        self.hardware = self._extract_labeled_variable(labeled_vars, constants.HARDWARE_KEY)
        self.partners = self._extract_labeled_variable(labeled_vars, constants.PARTNERS_KEY)
        self.revision = self._extract_labeled_variable(labeled_vars, constants.REVISION_KEY)
        self.used_by = self._extract_labeled_variable(labeled_vars, constants.USED_BY_KEY)
        self.red_black_swap = self._extract_labeled_variable(labeled_vars, constants.RED_BLACK_SWAP_KEY)
        self.zone = self._extract_labeled_variable(labeled_vars, constants.ZONE_KEY)


    def _extract_labeled_variable(self, labeled_variable_string, label_key):
        label_matcher = re.compile(".*?-" + label_key + constants.LABELED_VAR_SEPARATOR + "([" + constants.NAME_CHARS + "]*).*?$").match(labeled_variable_string)
        if label_matcher:
            return label_matcher.group(1)
        return None

    def next_group_name(self):
        return "%s-v%03d" % (self.cluster, (self.sequence + 1) if self.sequence is not None else 0)