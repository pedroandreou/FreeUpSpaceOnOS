import os


# Clean up APT cache
os.system("sudo du -sh /var/cache/apt")
os.system("sudo apt-get clean")

# Clear systemd journal logs
os.system("journalctl --disk-usage")
os.system("sudo journalctl --vacuum-time=3d")

# Remove older versions of Snap applications
os.system("du -h /var/lib/snapd/snaps")
