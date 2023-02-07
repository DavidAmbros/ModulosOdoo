# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas (Calendario)",  # Module title
    'description': """Lista de tareas en formato calendario""",  # You can also rst format
    'author': "",
    'website': "",
    'category': 'Project',
    'version': '1.0',
    'application': True,
    #Importante! Se basa en toda la estructura de project de Odoo
    #https://www.odoo.com/documentation/15.0/es/applications/services/project.html
    'depends': ['project'],
    'data': [
        'views/view_tareasCopy.xml',
        'views/view_tareas.xml',

    ],
}
