import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]


def build_site(destination: Path, token: str | None = None) -> None:
    env = os.environ.copy()
    if token is None:
        env.pop("CF_WEB_ANALYTICS_TOKEN", None)
    else:
        env["CF_WEB_ANALYTICS_TOKEN"] = token

    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "--site-dir", str(destination)],
        cwd=ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )


def test_local_build_does_not_include_analytics(tmp_path: Path):
    destination = tmp_path / "site"
    build_site(destination)

    homepage = (destination / "index.html").read_text()
    tutorial = (destination / "tutorials/index.html").read_text()
    assert "static.cloudflareinsights.com/beacon.min.js" not in homepage
    assert "static.cloudflareinsights.com/beacon.min.js" not in tutorial


def test_production_build_includes_analytics_on_homepage_and_tutorial(tmp_path: Path):
    destination = tmp_path / "site"
    build_site(destination, token="test-token")

    homepage = (destination / "index.html").read_text()
    tutorial = (destination / "tutorials/index.html").read_text()
    for page in (homepage, tutorial):
        assert "https://static.cloudflareinsights.com/beacon.min.js" in page
        assert 'data-cf-beacon=\'{"token":"test-token"}\'' in page
