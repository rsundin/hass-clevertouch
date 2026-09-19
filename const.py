"""Constants for the Clever Touch E3 integration."""
from clevertouch.devices import TempUnit
from homeassistant.const import UnitOfTemperature
from collections import namedtuple

DOMAIN = "clevertouch"

TEMP_NATIVE_UNIT = TempUnit.CELSIUS
TEMP_HA_UNIT = UnitOfTemperature.CELSIUS
TEMP_NATIVE_STEP = 0.5
TEMP_NATIVE_MIN = 5.0
TEMP_NATIVE_MAX = 30
TEMP_NATIVE_PRECISION = 0.1

DEFAULT_SCAN_INTERVAL_SECONDS = 180
QUICK_SCAN_INTERVAL_SECONDS = 15
QUICK_SCAN_COUNT = 3

# The OpenID (Keycloak) realm used for authentication differs per brand and is
# not derivable from the API host, so it is stored explicitly for each model.
Model = namedtuple("Model", ["manufacturer", "app", "url", "controller", "realm"])

DEFAULT_MODEL_ID = "purmo"
MODELS = {
    "purmo": Model("Purmo", "CleverTouch", "e3.lvi.eu", "Touch E3", "purmo"),
    "waltermeier": Model(
        "Walter Meier",
        "Walter Meier Smart-Comfort",
        "www.smartcomfort.waltermeier.com",
        "Metalplast Smart-Comfort",
        "purmo",
    ),
    "frico": Model(
        "Frico",
        "Frico FP Smart",
        "fricopfsmart.frico.se",
        "Central Unit",
        "purmo",
    ),
    "fenix": Model(
        "Fenix",
        "Fenix V24 Wifi",
        "v24.fenixgroup.eu",
        "Smart Home Controller",
        "fenix",
    ),
    "vogelundnoot": Model(
        "Vogel & Noot",
        "Vogel & Noot E3",
        "e3.vogelundnoot.com",
        "Touch E3",
        "purmo",
    ),
    "cordivari": Model(
        "Cordivari",
        "Cordivari My Way",
        "cordivarihome.com",
        "My Way",
        "purmo",
    ),
}
