{
    'name' : 'Project Custom',
    'version': '1.1',
    'category': 'Project',
    'author': 'Gerlin Matos',
    'depends' : ['base','project', 'stock', 'hr'],
    'description': """
Add custom fields project task.
    """,
    'data': [
        'views/project_task.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
