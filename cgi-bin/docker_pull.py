#!/usr/bin/env python3
import subprocess

print("Content-Type: text/html\n")

try:
    # Run the Docker pull command with sudo
    result = subprocess.run(["sudo", "docker", "pull", "centos:7"], capture_output=True, text=True, check=True)
    print("Docker pull successful.")

    # Gather information about the pulled image
    image_info = subprocess.run(["sudo", "docker", "inspect", "centos:7"], capture_output=True, text=True, check=True)
    image_info_lines = image_info.stdout.splitlines()

    # Extract and display relevant image details
    image_name = None
    image_os = None
    image_architecture = None
    
    for line in image_info_lines:
        if "RepoTags" in line:
            image_name = line.split(": ")[1]
        elif "Os" in line:
            image_os = line.split(": ")[1]
        elif "Architecture" in line:
            image_architecture = line.split(": ")[1]

    print("<h2>Image Details:</h2>")
    if image_name:
        print(f"<p><strong>Image Name:</strong> {image_name}</p>")
    if image_os:
        print(f"<p><strong>Operating System:</strong> {image_os}</p>")
    if image_architecture:
        print(f"<p><strong>Architecture:</strong> {image_architecture}</p>")
except subprocess.CalledProcessError as e:
    print(f"Error: {e.stderr}")
