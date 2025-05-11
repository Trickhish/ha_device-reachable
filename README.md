# Home Assistant - Ping component

### What does it do ?
Allows the user to create an entity for a device that follows its presence on the network.

&nbsp;
### What can it be used for ?
- To check if a server/NAS is online
- To register losses of service during the day
- To send notifications when a device goes offline
- To have logs of people entering and leaving the network

&nbsp;
### How to install ?
#### Method 1 (Manual) :
- Clone the repository or download it as a zip file
- Move the `custom_components/device_reachable` folder into the `config/custom_components` directory of HomeAssistant. It usually is at `~/homeassistant/` or `$USER/homeassistant/`.
- Restart HomeAssistant. (If using docker: `docker restart homeassistant`)

#### Method 2 (HACS) :
If you have installed the HACS module, the installation is way simpler.
- Go to the HACS tab
- Click on the 3 dots icon in the top-right corner
- Click on `Custom Repositories`
- Paste `https://github.com/Trickhish/ha_device-reachable` in the `repo` field.
- Select `Integration` as the type
- Restart HomeAssistant