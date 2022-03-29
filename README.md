# mdpublish
Publishing from Markdown into book form via Bindery.js

## Usage
1. Download `mdpublish.py` and place it in a directory named `mdpublish`.
2. Install `markdown` using `pip install markdown`.
3. Point `mdpublish.py` at a file: `py mdpublish.py file.md`.
4. Specify the following options: `--directory` to publish from a directory containing multiple files, `--author` to specify the name of the author, `--title` to specify the title of the book, `--cover` to generate a cover page automatically.
5. Output (a `.html` file) will be placed in the `dist` folder of the `mdpublish` directory.
