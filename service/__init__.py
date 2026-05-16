"""
Customer Accounts Service Package
"""
import sys
import logging
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from flask_talisman import Talisman
from flask_cors import CORS

# Security: Talisman headers and CORS policy
talisman = Talisman(app, force_https=False)
CORS(app)
# Create Flask application
app = Flask(__name__)
app.config.from_object("service.config") if False else None

# Basic config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///accounts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["LOGGING_LEVEL"] = logging.INFO

# Security: Talisman headers and CORS policy
talisman = Talisman(app, force_https=False)
CORS(app)
# ----------------------------------------------------------------------------
# Security Configuration: Talisman headers + CORS policy
# ----------------------------------------------------------------------------
# Talisman enforces HTTPS-related and content-security headers on every
# response. force_https=False is set for local dev / containerized testing;
# flip to True behind a TLS-terminating proxy in production.
talisman = Talisman(
    app,
    force_https=False,
    strict_transport_security=True,
    session_cookie_secure=False,
    content_security_policy={
        "default-src": "'self'",
        "img-src": "*",
    },
    frame_options="SAMEORIGIN",
    content_security_policy_nonce_in=["script-src"],
)

# CORS allows browser-based clients on other origins to call the API.
# "*" is fine for a public API; lock it down to specific origins for internal use.
CORS(app, resources={r"/*": {"origins": "*"}})

# Import routes AFTER app is created to avoid circular imports
from service import routes, models  # noqa: F401, E402
from service.common import error_handlers  # noqa: F401, E402

# Initialize the database
with app.app_context():
    models.db.create_all()

app.logger.info("Service initialized")
