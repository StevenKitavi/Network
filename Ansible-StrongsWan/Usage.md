# StrongSwan Ansible Playbook: Usage Guide

## Directory Structure

Create the following directory structure for your Ansible project:

```
strongswan-ansible/
├── inventory.ini
├── install_strongswan.yml
└── templates/
    ├── ipsec.conf.j2
    ├── ipsec.secrets.j2
    └── charon.conf.j2
```

## Configuration

1. Copy the playbook YAML content into the `install_strongswan.yml` file.
2. Copy each template file content into the corresponding files in the `templates` directory.
3. Edit the `inventory.ini` file to include your target server(s).
4. Modify the variables in the playbook to customize your VPN configuration:
   - `vpn_subnet`: The IP range to assign to VPN clients
   - `dns_servers`: DNS servers to provide to VPN clients
   - `vpn_clients`: User credentials for VPN authentication

## Important Security Notes

1. **DO NOT use the default passwords** in the example. Replace them with strong, unique passwords.
2. Consider using Ansible Vault to encrypt sensitive information.
3. The current configuration uses PSK (Pre-Shared Key) authentication. For production environments, consider implementing certificate-based authentication.

## Running the Playbook

Execute the playbook with:

```bash
ansible-playbook -i inventory.ini install_strongswan.yml
```

## Post-Installation

After running the playbook:

1. Verify that StrongSwan is running:
   ```bash
   systemctl status strongswan
   ```

2. Check the IPsec connections:
   ```bash
   ipsec statusall
   ```

3. Test the VPN connection from a client device.

## Troubleshooting

- Check logs with:
  ```bash
  journalctl -u strongswan
  cat /var/log/charon.log
  ```

- Ensure firewall rules are properly configured:
  ```bash
  iptables -L -v
  ```

- For persistent issues, increase the debug level in `ipsec.conf` and restart the service.

## Client Configuration

### Android
1. Install the "StrongSwan VPN Client" app from the Play Store
2. Create a new VPN profile with:
   - Server: Your server's public IP
   - VPN Type: IKEv2 EAP
   - Username and password from your `vpn_clients` configuration

### iOS
1. Go to Settings > General > VPN > Add VPN Configuration
2. Select IKEv2
3. Enter your server's public IP and the credentials from `vpn_clients`

### Windows 10/11
1. Go to Settings > Network & Internet > VPN > Add a VPN connection
2. Set VPN Provider to "Windows (built-in)"
3. Connection name: Choose any name
4. Server name or address: Your server's public IP
5. VPN type: IKEv2
6. Type of sign-in info: Username and password
7. Enter credentials from your `vpn_clients` configuration

### macOS
1. Go to System Preferences > Network
2. Click the "+" button to add a new service
3. Interface: VPN, VPN Type: IKEv2
4. Service Name: Choose any name
5. Server Address: Your server's public IP
6. Remote ID: Your server's public IP
7. Local ID: Leave blank
8. Authentication Settings: Username and password from `vpn_clients`

## Maintenance and Updates

- Periodically update StrongSwan:
  ```bash
  ansible-playbook -i inventory.ini install_strongswan.yml --tags update
  ```

- To add new VPN users, update the `vpn_clients` variable in the playbook and run:
  ```bash
  ansible-playbook -i inventory.ini install_strongswan.yml --tags config
  ```

- Monitor server performance and VPN connections regularly to ensure smooth operation.