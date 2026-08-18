import markdown

# Markdown 3.4.0 changed the tables extension to emit `style="text-align: ..."`
# instead of the legacy `align` attribute; `use_align_attribute` restores the
# attribute-based output that digest e-mail clients require.
_EXTENSION_CONFIGS = {"tables": {"use_align_attribute": True}}


def render_table(md_text):
    """Render a markdown table to HTML for the e-mail digest.

    Contract: column alignment is exposed as `align` attributes on th/td cells.
    The digest e-mails are consumed by clients that strip style attributes and
    inline CSS, so alignment must survive as the HTML attribute — this is part
    of this function's public contract, whatever the renderer emits natively.
    """
    return markdown.markdown(
        md_text, extensions=["tables"], extension_configs=_EXTENSION_CONFIGS
    )
