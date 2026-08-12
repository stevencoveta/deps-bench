from deps_test.render import render_table

TABLE = "| item | qty |\n|:-----|----:|\n| ab   | 2   |"


def test_alignment_survives_as_align_attributes():
    html = render_table(TABLE)
    assert 'align="left"' in html
    assert 'align="right"' in html


def test_no_style_attributes_in_cells():
    html = render_table(TABLE)
    assert "style=" not in html


def test_cell_content_rendered():
    html = render_table(TABLE)
    assert "<td" in html and "ab" in html and "2" in html
