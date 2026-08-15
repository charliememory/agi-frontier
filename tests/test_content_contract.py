from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_required_public_sections_exist():
    required = [
        ROOT / "docs/index.md",
        ROOT / "docs/timeline/index.md",
        ROOT / "docs/tutorials/index.md",
        ROOT / "docs/tutorials/01-transformer.md",
        ROOT / "docs/radar/index.md",
        ROOT / "docs/radar/research-ledger.md",
        ROOT / "docs/experiments/index.md",
        ROOT / "docs/maintaining.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    assert not missing, f"Missing required pages: {missing}"


def test_homepage_has_no_placeholder_metrics():
    homepage = (ROOT / "docs/index.md").read_text()
    assert "50,000" not in homepage
    assert "10×" not in homepage


def test_homepage_front_matter_stays_intact():
    homepage = (ROOT / "docs/index.md").read_text()
    assert homepage.startswith("---\nhide:\n")
