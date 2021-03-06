from . import GraphTemplate

class SwiftTempauthTemplate(GraphTemplate):
    pattern_graph = "^stats\.([^\.]+)\.tempauth\.AUTH_\.errors$"
    target_types = {
        'swift_tempauth_rate': {
            'match': '^stats\.(?P<server>[^\.]+)\.tempauth\.AUTH_\.(?P<type>[^\.]+)$',
            'default_group_by': 'server'
        },
        'swift_tempauth_count': {
            'match': '^stats_counts\.(?P<server>[^\.]+)\.tempauth\.AUTH_\.(?P<type>[^\.]+)$',
            'default_group_by': 'server'
        }
    }

    def generate_graphs(self, match):
        return {}

# vim: ts=4 et sw=4:
