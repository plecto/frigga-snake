from frigga_snake.constants import APP_VERSION_PATTERN


class AMIName(object):
    def __init__(self, ami_name, ami_description, app_version):
        app_version_matcher = APP_VERSION_PATTERN.match(app_version)
        if not app_version_matcher:
            return
        self.package_name = app_version_matcher.group(1)
        self.version = app_version_matcher.group(2)
        self.build_number = "".join(app_version_matcher.group(3)[1:]) if app_version_matcher.group(3).startswith("h") and app_version_matcher.group(3) else app_version_matcher.group(4)
        self.commit = app_version_matcher.group(4) if app_version_matcher.group(3).startswith("h") and app_version_matcher.group(3) else app_version_matcher.group(3)
        self.build_job_name = app_version_matcher.group(5)

    def __str__(self):
        return "AppVersion [package_name=%s,version=%s,build_job_name=%s,build_number=%s,commit=%s" % (
            self.package_name,
            self.version,
            self.build_job_name,
            self.build_number,
            self.commit
        )

    def __repr__(self):
        return "<AMIName %s>" % str(self)
