import subprocess
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.core import callback

from .const import DOMAIN, CONF_IP_ADDRESS, CONF_NAME

async def async_setup_entry(hass, config_entry, async_add_entities):
    name = config_entry.data[CONF_NAME]
    ip = config_entry.data[CONF_IP_ADDRESS]
    async_add_entities([ComputerReachableSensor(name, ip)], True)

class ComputerReachableSensor(BinarySensorEntity):
    def __init__(self, name, ip):
        self._attr_name = name
        self._attr_unique_id = f"computer_reachable_{ip.replace('.', '_')}"
        self._ip = ip
        self._attr_device_class = "connectivity"
        self._attr_is_on = False

    def update(self):
        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1", self._ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            self._attr_is_on = result.returncode == 0
        except Exception:
            self._attr_is_on = False
