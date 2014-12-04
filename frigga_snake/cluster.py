from frigga_snake.names import Names


class Cluster(object):
    @staticmethod
    def group_by_cluster_name(asg_names):
        clusters = {}
        for asg_name in asg_names:
            n = Names(asg_name)
            if n.cluster not in clusters:
                clusters[n.cluster] = []
            clusters[n.cluster].append(asg_name)
        return clusters