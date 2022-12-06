{
    "name": "NEG Shield Possibility",
    "summary": """Product no add access""",
    "version": "15.0.1.0.0",
    "category": "",
    "description": u"""
""",
    "author": "Cravit",
    "website": "https://www.cravit.nl",
    "depends": [
        "account",
        "base",
        "sale",
        "purchase",
    ],
    "data": [
        "views/product_no_create_view.xml",
    ],
    "assets": {
        'web.assets_backend': ['product_no_create/static/src/js/no_quick_create.js'],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "OPL-1",
}
