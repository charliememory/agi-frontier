import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]


def build_site(destination: Path) -> None:
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "--site-dir", str(destination)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def test_build_includes_analytics_on_homepage_and_tutorial(tmp_path: Path):
    destination = tmp_path / "site"
    build_site(destination)

    homepage = (destination / "index.html").read_text()
    tutorial = (destination / "tutorials/index.html").read_text()
    for page in (homepage, tutorial):
        assert "https://static.cloudflareinsights.com/beacon.min.js" in page
        assert 'data-cf-beacon=\'{"token":"bd8e7715fb654049b3dc01af5dcbd216"}\'' in page
