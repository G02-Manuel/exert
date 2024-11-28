{
    'name' : 'Project Custom',
    'version': '1.1',
    'category': 'Project',
    'author': 'Gerlin Matos',
    'depends' : ['base','project', 'stock', 'hr'],
    'description': """
Add custom fields project task and employee
    """,
    'data': [
        'data/ir_filters.xml',
        'views/project_task.xml',
        'views/hr_employee.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
