import markdown
import argparse
import os
import glob

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>%TITLE%</title>
</head>
<body>
<div id='content'>
%CONTENT%
</div>
<script src='https://unpkg.com/bindery@2.3.6/dist/bindery.min.js'></script>
<script>
let runningHeaders = Bindery.RunningHeader({
  render: (page) => {
  if (!(page.number == %CONTENT_START% )){
  return page.isLeft ? `${page.number} - %AUTHOR%` : `%TITLE% - ${page.number}`
  }else{
  return ``}
  }
});

Bindery.makeBook({
content: '#content',
rules: [
      Bindery.PageBreak({ selector: 'h1', position: 'before' }),
      Bindery.FullBleedSpread({ selector: '.big-figure' }),
      runningHeaders
    ],
});
</script>
</body>
</html>
'''


DIRECTORY_MODE = False
OUTPUT = os.getcwd() + '/dist'
TITLE = 'Compiled Document'
AUTHOR = 'Anonymous'
CONTENT_START = 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generating books from markdown files or directories.')
    parser.add_argument('target', help='Markdown file or directory to convert from.')
    parser.add_argument('--directory', '-d', help='Target is a directory.', action='store_true')
    parser.add_argument('--title', '-t', help='Title for the compiled book.')
    parser.add_argument('--author', '-a', help='Author for the compiled book.')
    parser.add_argument('--cover', '-c', help='Whether to generate a cover for the book.', action='store_true')
    args = parser.parse_args()

    if args.directory:
        DIRECTORY_MODE = True

    source_text = []

    if DIRECTORY_MODE:
        file_list = [os.path.normpath(filename) for filename in glob.iglob(args.target + '/*.md')]
        for file in file_list:
            with open(file) as f:
                source_text.append(f.read())
    else:
        with open(args.target) as f:
            source_text.append(f.read())
    if args.title:
        TITLE = args.title
    if args.author:
        AUTHOR = args.author
    if args.cover:
        CONTENT_START = 1
        source_text.insert(0, '# '+TITLE+'\n'+'*By '+AUTHOR+'*')
    os.makedirs(OUTPUT, exist_ok=True)
    with open(os.path.normpath(OUTPUT+'/'+TITLE+'.html'), 'w+') as f:
        page_content = HTML_TEMPLATE
        page_content = page_content.replace('%TITLE%', TITLE)
        page_content = page_content.replace('%AUTHOR%', AUTHOR)
        page_content = page_content.replace('%CONTENT_START%', str(CONTENT_START))
        page_content = page_content.replace('%CONTENT%', markdown.markdown('\n'.join(source_text)))
        f.write(page_content)