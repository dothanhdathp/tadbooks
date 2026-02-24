def define_env(env):
    @env.macro
    def book_card(name, img_path, markdown_link):
        if markdown_link == "":
            return f'''- ![]({img_path}){{.small-icon}} <p>{name}</p>'''
        else:
            return f'''- [![]({img_path}){{.small-icon}}]({markdown_link}) <p>{name}</p>'''