from typing import Any

space_ids = {
    'PICOE-DEV': '2f35885d-0c9d-4423-83ad-fd05066f8576',
}

fake_pcf_call: list[dict[str, Any]] = [
    {
        'org_id': '123456789',
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': '1cb006ee-fb05-47e1-b541-c34179ddc446',
                'name': 'pi-services-viewpoint',
                'desired_state': 'RUNNING',
                'total_desired_instances': 0,
                'created_at': '2025-03-17T21:41:30Z',
                'updated_at': '2025-06-08T16:41:26Z',
                'lifecycle': {
                    'type': 'buildpack',
                    'data': {
                        'buildpack': 'python_buildpack_1_7_14',
                        'stack': 'cflinuxfs2',
                    },
                },
                'environment_variables': {'HTTP_PROXY': 'http://proxy.example.com'},
                'links': {
                    'self': {
                        'href': 'https://api.example.org/v3/apps/1cb006ee-fb05-47e1-b541-c34179ddc446'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-DEV"]}'
                    },
                    'processes': {
                        'href': 'https://api.example.org/v3/apps/1cb006ee-fb05-47e1-b541-c34179ddc446/processes'
                    },
                    'route_mappings': {
                        'href': 'https://api.example.org/v3/apps/1cb006ee-fb05-47e1-b541-c34179ddc446/route_mappings'
                    },
                    'packages': {
                        'href': 'https://api.example.org/v3/apps/1cb006ee-fb05-47e1-b541-c34179ddc446/packages'
                    },
                    'droplet': {
                        'href': 'https://api.example.org/v3/apps/1cb006ee-fb05-47e1-b541-c34179ddc446/droplets/current'
                    },
                    'droplets': {
                        'href': 'https://api.example.org/v3/apps/1cb006ee-fb05-47e1-b541-c34179ddc446/droplets'
                    },
                    'tasks': {
                        'href': 'https://api.example.org/v3/apps/1cb006ee-fb05-47e1-b541-c34179ddc446/tasks'
                    },
                    'start': {
                        'href': 'https://api.example.org/v3/apps/1cb006ee-fb05-47e1-b541-c34179ddc446/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': 'https://api.example.org/v3/apps/1cb006ee-fb05-47e1-b541-c34179ddc446/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
]
