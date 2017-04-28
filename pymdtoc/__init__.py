import copy

class TOC(object):
    def __init__(self, file=None, lines=None,
                 toc_heading='Table of contents',
                 anchor_function=None):

        if not file and not lines:
            raise Exception('No data found')

        self.content = None
        if file:
            f = open(file)
            self.content = f.readlines()
            lines = [line.strip() for line in self.content]

        self.toc_heading = toc_heading
        self.headings = []
        for line in lines:
            if line.startswith("#"):
                if line.lstrip("#").lstrip() != self.toc_heading:
                    self.headings.append(line)

        def get_anchor(heading):
            heading = heading.lower().lstrip().replace(" ", "-")
            heading = "".join([h for h in heading if h.isalnum() or h in [' ', '-']])
            return "#{}".format(heading)

        self.anchor_function = get_anchor if anchor_function is None else anchor_function
        if len(self.headings) > 0:
            self.toc = self.build_toc()

        if self.content:
            self.content = self.build_content()


    def build_toc(self):
        '''
        Generate markdown style TOC.
        '''

        def get_hc(heading):
            return heading.count('#') - 1

        toc = ["# {}".format(self.toc_heading)]
        hc = get_hc(self.headings[0])

        for head in self.headings:
            spacing = " " * (get_hc(head) * 4)
            title = head.lstrip("#").lstrip()
            toc.append("{}- [{}]({})".format(spacing,
                                            title,
                                            self.anchor_function(title)))

        return "\n".join(toc)


    def build_content(self):
        '''
        Content now contains TOC.
        '''
        content = copy.deepcopy(self.content)
        if len(self.headings) > 0:
            start = 0

            if content[0].strip() == "<!-- starttoc -->":
                for line in content:
                    start += 1
                    if line.strip() == "<!-- endtoc -->":
                        break

            content = "<!-- starttoc -->\n" +\
                      self.toc +\
                      "\n\n<!-- endtoc -->" + '\n\n' +\
                      "".join(content[start+1:])

        return content
