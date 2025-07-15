# Release Scripts

This directory contains scripts to help with releasing the Thriving API Python SDK.

## release.py

Automated release script that:
1. Updates the changelog
2. Creates a git tag
3. Pushes to GitHub
4. Creates a GitHub release
5. Triggers automatic PyPI publishing via GitHub Actions

### Usage

```bash
# Patch release (bug fixes)
python scripts/release.py 1.0.5 "Fixed MRO issues and improved error handling" --patch

# Minor release (new features)  
python scripts/release.py 1.1.0 "Added new AI analysis endpoints" --minor

# Major release (breaking changes)
python scripts/release.py 2.0.0 "Complete API redesign with breaking changes" --major

# Default (patch release)
python scripts/release.py 1.0.5 "Bug fixes and improvements"
```

### What happens automatically:

1. **Script actions:**
   - Updates `CHANGELOG.md` with new version and notes
   - Commits changelog changes
   - Creates git tag (e.g., `v1.0.5`)
   - Pushes tag to GitHub
   - Creates GitHub release

2. **GitHub Actions (automatic):**
   - Extracts version from git tag
   - Updates `pyproject.toml` and `src/thriving_api/__init__.py` with tag version
   - Builds package with correct version
   - Publishes to PyPI automatically

### Benefits:

- ✅ **No manual version updates** - Version comes from git tag
- ✅ **Consistent versioning** - Same version across all files
- ✅ **Automatic PyPI publishing** - No manual upload needed
- ✅ **Clean build process** - Removes old artifacts before building
- ✅ **Version verification** - Ensures built package has correct version
- ✅ **Changelog automation** - Automatically updates changelog

### Requirements:

- `gh` CLI tool installed and authenticated
- Git repository with proper remote setup
- PyPI API token configured in GitHub secrets
