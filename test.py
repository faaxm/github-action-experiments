import os
from pathlib import Path
import subprocess


def run_command(cmd):
    print(f"\n\n\n\n### Running command: {cmd}", flush=True)
    subprocess.run(cmd, check=True)

def find_latest_makeappx():
    # Define the base path for Windows Kits
    base_path = Path("C:/Program Files (x86)/Windows Kits/10/bin")
    if not base_path.exists():
        print("Windows Kits directory not found.")
        return None

    # Collect all version directories under the base path
    version_dirs = [d for d in base_path.iterdir() if d.is_dir() and d.name.replace('.', '').isdigit()]
    if not version_dirs:
        print("No version directories found in Windows Kits.")
        return None

    # Sort directories by version number (higher is newer)
    version_dirs.sort(key=lambda d: [int(part) for part in d.name.split('.')], reverse=True)

    # Check for MakeAppx.exe in the x64 subdirectory of the latest version
    for version_dir in version_dirs:
        makeappx_path = version_dir / "x64" / "MakeAppx.exe"
        if makeappx_path.exists():
            print(f"Found MakeAppx.exe at: {makeappx_path}")
            return str(makeappx_path)

    print("MakeAppx.exe not found in any version directory.")
    return None


if __name__ == "__main__":
    makeappx_path = find_latest_makeappx()
    if makeappx_path:
        print(f"The latest MakeAppx.exe is located at: {makeappx_path}")
        run_command([makeappx_path, "pack"])
    else:
        print("MakeAppx.exe could not be found.")