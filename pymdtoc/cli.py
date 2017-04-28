import fire

from __init__ import TOC


class TOCcli(object):
    def generate(self, filename):
        toc = TOC(file=filename)
        return toc.content

    def inplace(self, filename):
        content = self.generate(filename)
        with open(filename, 'w') as f:
            f.write(content)

def cli():
    fire.Fire(TOCcli)

if __name__ == '__main__':
    cli()
