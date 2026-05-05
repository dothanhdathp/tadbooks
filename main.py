def define_env(env):
    @env.macro
    def book_card(name, img_path, markdown_link):
        if markdown_link == "":
            return f'''- ![]({img_path}){{.small-icon}} <p>{name}</p>'''
        else:
            return f'''- [![]({img_path}){{.small-icon}}]({markdown_link}) <p>{name}</p>'''

    @env.macro
    def book_detail(name, img_path, author, detail):
        return f'''<div class="grid cards" markdown><div class="grid-item" style="text-align: center; width: 20%;" markdown>

![]({img_path}){{.medium-icon}}
    
</div><div class="grid-item" style="text-align: left; width: 70%;" markdown>
    
<div class="grid-item" style="font-size: 1rem" markdown>{name}</div>

**Tác Giả**: {author}

{detail}

</div>
</div>'''

    @env.macro
    def linkslide(title, link_html):
        return f'''<a href="javascript:void(0);" onclick="openSlide('http://localhost:65000/{link_html}')">⧉ {title}</a>'''
    
    @env.macro
    def slide(link_html, isfull=False):
        if isfull:
            return f'''<iframe src="http://localhost:65000/{link_html}" style="width: 100%; aspect-ratio: 16 / 9; border: none;" allowfullscreen></iframe>'''
        else:
            return f'''<div style="text-align: center;">
                <iframe 
                    src="http://localhost:65000/{link_html}" 
                    style="width: 960px; aspect-ratio: 16 / 9; border: none;"
                    allowfullscreen>
                </iframe>
            </div>'''
    
    @env.macro
    def book(title, book, page=""):
        return f'''[{title}](http://localhost:65000/book/{book}/{page})'''