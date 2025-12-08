from typing import Any

org_ids = {
    'PICOE': '1c845df9-a375-414c-8d69-4133363d9c03',
    'PICOEFIN': '9259380c-aa2e-4fb4-9ef2-26408c25fd62',
    'AIDEN': 'd8a5618a-95ba-4466-89e8-0c8a0fda8673',
    'WHATIF': '574c0903-ac6e-436a-a231-19aa4acaa52e',
    'MEMALPHA': '51b0c378-e4f0-4704-b724-d12c17b20614',
}

org_names = {
    '1c845df9-a375-414c-8d69-4133363d9c03': 'PICOE',
    '9259380c-aa2e-4fb4-9ef2-26408c25fd62': 'PICOEFIN',
    'd8a5618a-95ba-4466-89e8-0c8a0fda8673': 'AIDEN',
    '574c0903-ac6e-436a-a231-19aa4acaa52e': 'WHATIF',
    '51b0c378-e4f0-4704-b724-d12c17b20614': 'MEMALPHA',
}

space_ids = {
    'PICOE-PRD': '2f35885d-0c9d-4423-83ad-fd05066f8576',
    'PICOE-PRD-STATIC': 'a6cfa3fa-4001-4422-bd2e-2a515349c4ca',
    'PICOEFIN-PRD': 'c8eeabaf-ea99-4620-be01-e83af8894c75',
    'PICOEFIN-PRD-STATIC': 'ec0f7dcb-b313-4d71-a964-6e8cacbef2ed',
    'AIDEN-PRD': '6e414b78-e1dc-4845-afd3-a0e513367427',
    'AIDEN-PRD-STATIC': '04b3da5d-4869-4cf4-8c79-2486e0de00ad',
    'WHATIF-PRD': '2757a327-1a5b-4992-995c-8986e2bf525c',
    'WHATIF-PRD-STATIC': 'a6d336cb-459b-4a32-b46e-126d18941df4',
    'MEMALPHA-PRD': 'f5ffd863-2930-436b-b36b-8e095fd25626',
    'MEMALPHA-PRD-STATIC': '2cf9ecde-6487-4b1a-8253-6adc0a723bd2',
}

spaces_by_id = {
    '2f35885d-0c9d-4423-83ad-fd05066f8576': 'PRD',
    'a6cfa3fa-4001-4422-bd2e-2a515349c4ca': 'PRD-STATIC',
    'c8eeabaf-ea99-4620-be01-e83af8894c75': 'PRD',
    'ec0f7dcb-b313-4d71-a964-6e8cacbef2ed': 'PRD-STATIC',
    '6e414b78-e1dc-4845-afd3-a0e513367427': 'PRD',
    '04b3da5d-4869-4cf4-8c79-2486e0de00ad': 'PRD-STATIC',
    '2757a327-1a5b-4992-995c-8986e2bf525c': 'PRD',
    'a6d336cb-459b-4a32-b46e-126d18941df4': 'PRD-STATIC',
    'f5ffd863-2930-436b-b36b-8e095fd25626': 'PRD',
    '2cf9ecde-6487-4b1a-8253-6adc0a723bd2': 'PRD-STATIC',
}


app_ids = {
    'actions-reminders': '09677995-1651-4697-aa59-2ecf375de7bc',
    'staff-viewer': '1bc142c1-6f70-4104-a18f-155636eef23a',
    'viewpoint': 'e8ac607c-e8f2-4abf-b2a2-13ccf58ff09c',
    'performance-management': '62f40f15-cda5-44ee-a694-601d8acf3591',
    'reporting-hub': '7e98a6b8-d8d5-46ba-9905-2d3fda8291b6',
    'pi-services-viewpoint': '1cb006ee-fb05-47e1-b541-c34179ddc446',
    'pi-services-performance-management': '1833a87b-68b5-4c74-950d-98b0feb9029a',
    'pi-services-reporting-hub': '2e8fc6dc-9031-4804-9e7a-18f8b242a82b',
    'cost-allocations': '8560b4b5-b1cc-4957-8b54-1e07fd4f8a63',
    'cost-insights': '73fb06e6-668d-459c-8869-2b06b8b7af46',
    'pi-services-cost-allocations': '167f8cc5-3373-46fa-9c32-bbfa08d9ba80',
    'pi-services-cost-insights': '0b378e12-5878-46c4-8fbf-57fc06805e88',
    'aiden': '6043bc8e-11ac-4e6c-bedb-0f53ed394657',
    'pi-services-aiden': '018c4122-11a2-441b-ae12-54b23a1814d5',
    'pi-services-aiden-rag': '73c20d05-98ad-4b24-b871-d4be79eef9e2',
    'whatif-core': 'a56ea34d-f79c-463f-95f4-ef779105af68',
    'whatif-core-backend': 'ec4a61a9-3555-45bb-adeb-b8f85204dd9c',
    'starfleet-archives': '05a505fa-603f-447c-a309-3d1e8f9239bc',
    'pi-services-starfleet-archives': '030ad9ea-b3aa-4052-aa65-52724eaa3ef9',
}

role_to_org_id = {
    'rPcf_PICOE': '1c845df9-a375-414c-8d69-4133363d9c03',
    'rPcf_PICOEFIN': '9259380c-aa2e-4fb4-9ef2-26408c25fd62',
    'rPcf_AIDEN': 'd8a5618a-95ba-4466-89e8-0c8a0fda8673',
    'rPcf_WHATIF': '574c0903-ac6e-436a-a231-19aa4acaa52e',
    'rPcf_MEMALPHA': '51b0c378-e4f0-4704-b724-d12c17b20614',
}


fake_pcf_call: list[dict[str, Any]] = [
    # PICOE - PRD-STATIC
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['actions-reminders'],
                'name': 'actions-reminders',
                'space_id': space_ids['PICOE-PRD-STATIC'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["actions-reminders"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['staff-viewer'],
                'name': 'staff-viewer',
                'space_id': space_ids['PICOE-PRD-STATIC'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["staff-viewer"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['viewpoint'],
                'name': 'viewpoint',
                'space_id': space_ids['PICOE-PRD-STATIC'],
                'desired_state': 'DOWN',
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["viewpoint"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['performance-management'],
                'name': 'performance-management',
                'space_id': space_ids['PICOE-PRD-STATIC'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["performance-management"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['reporting-hub'],
                'name': 'reporting-hub',
                'space_id': space_ids['PICOE-PRD-STATIC'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["reporting-hub"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # PICOE - PRD
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['pi-services-viewpoint'],
                'name': 'pi-services-viewpoint',
                'space_id': space_ids['PICOE-PRD'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-viewpoint"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['pi-services-performance-management'],
                'name': 'pi-services-performance-management',
                'space_id': space_ids['PICOE-PRD'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-performance-management"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOE'],
        'org_name': 'PICOE',
        'instances': [
            {
                'guid': app_ids['pi-services-reporting-hub'],
                'name': 'pi-services-reporting-hub',
                'space_id': space_ids['PICOE-PRD'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOE-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-reporting-hub"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # PICOEFIN - PRD-STATIC
    {
        'org_id': org_ids['PICOEFIN'],
        'org_name': 'PICOEFIN',
        'instances': [
            {
                'guid': app_ids['cost-allocations'],
                'name': 'cost-allocations',
                'space_id': space_ids['PICOEFIN-PRD-STATIC'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOEFIN-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-allocations"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOEFIN'],
        'org_name': 'PICOEFIN',
        'instances': [
            {
                'guid': app_ids['cost-insights'],
                'name': 'cost-insights',
                'space_id': space_ids['PICOEFIN-PRD-STATIC'],
                'desired_state': 'STARTING',
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOEFIN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["cost-insights"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # PICOEFIN - PRD
    {
        'org_id': org_ids['PICOEFIN'],
        'org_name': 'PICOEFIN',
        'instances': [
            {
                'guid': app_ids['pi-services-cost-allocations'],
                'name': 'pi-services-cost-allocations',
                'space_id': space_ids['PICOEFIN-PRD'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOEFIN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-allocations"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['PICOEFIN'],
        'org_name': 'PICOEFIN',
        'instances': [
            {
                'guid': app_ids['pi-services-cost-insights'],
                'name': 'pi-services-cost-insights',
                'space_id': space_ids['PICOEFIN-PRD'],
                'desired_state': 'STOPPED',
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["PICOEFIN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-cost-insights"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # AIDEN - PRD-STATIC
    {
        'org_id': org_ids['AIDEN'],
        'org_name': 'AIDEN',
        'instances': [
            {
                'guid': app_ids['aiden'],
                'name': 'aiden',
                'space_id': space_ids['AIDEN-PRD-STATIC'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["AIDEN-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["aiden"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # AIDEN - PRD
    {
        'org_id': org_ids['AIDEN'],
        'org_name': 'AIDEN',
        'instances': [
            {
                'guid': app_ids['pi-services-aiden'],
                'name': 'pi-services-aiden',
                'space_id': space_ids['AIDEN-PRD'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["AIDEN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    {
        'org_id': org_ids['AIDEN'],
        'org_name': 'AIDEN',
        'instances': [
            {
                'guid': app_ids['pi-services-aiden-rag'],
                'name': 'pi-services-aiden-rag',
                'space_id': space_ids['AIDEN-PRD'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["AIDEN-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-aiden-rag"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # WHATIF - PRD-STATIC
    {
        'org_id': org_ids['WHATIF'],
        'org_name': 'WHATIF',
        'instances': [
            {
                'guid': app_ids['whatif-core'],
                'name': 'whatif-core',
                'space_id': space_ids['WHATIF-PRD-STATIC'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["WHATIF-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # WHATIF - PRD
    {
        'org_id': org_ids['WHATIF'],
        'org_name': 'WHATIF',
        'instances': [
            {
                'guid': app_ids['whatif-core-backend'],
                'name': 'whatif-core-backend',
                'space_id': space_ids['WHATIF-PRD'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["WHATIF-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["whatif-core-backend"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # MEMALPHA - PRD-STATIC
    {
        'org_id': org_ids['MEMALPHA'],
        'org_name': 'MEMALPHA',
        'instances': [
            {
                'guid': app_ids['starfleet-archives'],
                'name': 'starfleet-archives',
                'space_id': space_ids['MEMALPHA-PRD-STATIC'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["MEMALPHA-PRD-STATIC"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["starfleet-archives"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
    # MEMALPHA - PRD
    {
        'org_id': org_ids['MEMALPHA'],
        'org_name': 'MEMALPHA',
        'instances': [
            {
                'guid': app_ids['pi-services-starfleet-archives'],
                'name': 'pi-services-starfleet-archives',
                'space_id': space_ids['MEMALPHA-PRD'],
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
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}'
                    },
                    'space': {
                        'href': f'https://api.example.org/v2/spaces/{space_ids["MEMALPHA-PRD"]}'
                    },
                    'processes': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/processes'
                    },
                    'route_mappings': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/route_mappings'
                    },
                    'packages': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/packages'
                    },
                    'droplet': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/droplets/current'
                    },
                    'droplets': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/droplets'
                    },
                    'tasks': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/tasks'
                    },
                    'start': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/start',
                        'method': 'PUT',
                    },
                    'stop': {
                        'href': f'https://api.example.org/v3/apps/{app_ids["pi-services-starfleet-archives"]}/stop',
                        'method': 'PUT',
                    },
                },
            },
        ],
    },
]
