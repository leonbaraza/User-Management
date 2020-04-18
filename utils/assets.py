from flask_assets import Environment, Bundle

bundles = {
    'admin_css' : Bundle(
        'css/navbar.css',
        'css/styles.css',
    )
} 