Display the local time to the nearest half-hour using the Unicode
analog clock-face code-points.

You can see the glyphs here:
http://www.unicode.org/charts/PDF/U1F300.pdf

...but most fonts don't support them yet, unfortunately.

Example:

python -c "import clockface; print clockface.glyph()"

License: GPLv3+
