{
	"name" : "Modulo de adicion de campos en el formulario CRM",
	"version" : "17.0.0.0",
	"category" : "CRM",
	"depends" : [
        'base',
		'crm'
    ],
	"author": "AppexBo",
	'summary': 'Modulo de adicion de campos en el formulario CRM',
	"description": "Modulo de adicion de campos en el formulario CRM",
	"website" : "https://www.appexbo.com/",
	
	"data": [
		'security/ir.model.access.csv',
		'views/portafolio/views.xml',
		'views/bu/views.xml',
		'views/crm/views.xml'
	],

	"application": False,
	"auto_install": False,
	"installable": True,
    "license": "LGPL-3",
}