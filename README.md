# ipmi-grain

Let physical servers figure out their ipmi ip, and provide it in a grain.

## Synopsis

After installation, you can run commands like this:

```yaml
# salt -G virtual:physical grains.item ipmi_ip
answers.example.org:
    ----------
    ipmi_ip:
        10.0.0.42
```

## Installation

Merge the following in /etc/salt/master.d/your.conf

```yaml
fileserver_backend:
  - roots
  - git

gitfs_remotes:
  - https://github.com/gerhardqux/ipmi-grain
```

Make sure to clone this repo close to your salt master, instead of running it from github directly.

Then sync the grain to your minions:

```bash
# salt '*' saltutil.sync_grains
```
