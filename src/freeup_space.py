import os


# Clean up APT cache
os.system("sudo du -sh /var/cache/apt")
os.system("sudo apt-get clean")

# Clear systemd journal logs
os.system("journalctl --disk-usage")
os.system("sudo journalctl --vacuum-time=3d")

# Remove older versions of Snap applications
os.system("du -h /var/lib/snapd/snaps")

# Empty trash bin
os.system("gio trash --empty")

# Use ncdu to see how much space each file holds
os.system("ncdu $HOME")
