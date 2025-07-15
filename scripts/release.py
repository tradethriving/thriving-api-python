#!/usr/bin/env python3
"""
Release script for Thriving API Python SDK

This script helps create releases with automatic version management.
The GitHub Actions workflow will automatically extract the version from the git tag.

Usage:
    python scripts/release.py 1.0.5 "Release notes here"
    python scripts/release.py 1.0.5 --patch "Bug fixes"
    python scripts/release.py 1.1.0 --minor "New features"
    python scripts/release.py 2.0.0 --major "Breaking changes"
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_command(cmd, check=True):
    """Run a shell command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error running command: {cmd}")
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result


def update_changelog(version, release_type, notes):
    """Update the CHANGELOG.md file with the new release."""
    changelog_path = Path("CHANGELOG.md")
    if not changelog_path.exists():
        print("CHANGELOG.md not found!")
        return
    
    # Read current changelog
    with open(changelog_path, 'r') as f:
        content = f.read()
    
    # Create new entry
    date = datetime.now().strftime("%Y-%m-%d")
    release_type_emoji = {
        'major': '🚀',
        'minor': '✨', 
        'patch': '🐛'
    }
    
    emoji = release_type_emoji.get(release_type, '📦')
    new_entry = f"""## [{version}] - {date}

### {release_type.title()} Release {emoji}
{notes}

"""
    
    # Insert after the header
    lines = content.split('\n')
    insert_index = 8  # After the header section
    
    lines.insert(insert_index, new_entry.strip())
    
    # Write back
    with open(changelog_path, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"✅ Updated CHANGELOG.md with version {version}")


def create_release(version, release_type, notes):
    """Create a new release."""
    
    # Ensure we're on main branch and up to date
    run_command("git checkout main")
    run_command("git pull origin main")
    
    # Update changelog
    update_changelog(version, release_type, notes)
    
    # Commit changelog changes
    run_command("git add CHANGELOG.md")
    run_command(f'git commit -m "📝 Update changelog for v{version}"')
    
    # Create and push tag
    run_command(f"git tag v{version}")
    run_command("git push origin main")
    run_command(f"git push origin v{version}")
    
    # Create GitHub release
    release_title = f"v{version} - {release_type.title()} Release"
    release_notes = f"""## {release_type.title()} Release

{notes}

## 📦 Installation
```bash
pip install --upgrade thriving-api
```

## 🔗 Links
- [PyPI Package](https://pypi.org/project/thriving-api/{version}/)
- [Full Changelog](https://github.com/tradethriving/thriving-api-python/blob/main/CHANGELOG.md)
- [API Documentation](https://docs.tradethriving.com/api)
"""
    
    # Escape quotes for shell command
    release_notes_escaped = release_notes.replace('"', '\\"').replace('`', '\\`')
    
    run_command(f'gh release create v{version} --title "{release_title}" --notes "{release_notes_escaped}"')
    
    print(f"""
🎉 Release v{version} created successfully!

The GitHub Actions workflow will now:
1. Extract version {version} from the git tag
2. Update pyproject.toml and __init__.py automatically
3. Build the package with version {version}
4. Publish to PyPI automatically

You can monitor the progress at:
https://github.com/tradethriving/thriving-api-python/actions
""")


def main():
    parser = argparse.ArgumentParser(description="Create a new release")
    parser.add_argument("version", help="Version number (e.g., 1.0.5)")
    parser.add_argument("notes", help="Release notes")
    parser.add_argument("--patch", action="store_const", const="patch", dest="release_type", help="Patch release (bug fixes)")
    parser.add_argument("--minor", action="store_const", const="minor", dest="release_type", help="Minor release (new features)")
    parser.add_argument("--major", action="store_const", const="major", dest="release_type", help="Major release (breaking changes)")
    
    args = parser.parse_args()
    
    # Default to patch if no type specified
    release_type = args.release_type or "patch"
    
    print(f"Creating {release_type} release v{args.version}")
    print(f"Release notes: {args.notes}")
    
    # Confirm
    response = input("Continue? (y/N): ")
    if response.lower() != 'y':
        print("Cancelled.")
        sys.exit(0)
    
    create_release(args.version, release_type, args.notes)


if __name__ == "__main__":
    main()
