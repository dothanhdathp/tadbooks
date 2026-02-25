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