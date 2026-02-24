def define_env(env):
    @env.macro

    def book_card(title, author, img_path, mdlink, description):
        if mdlink != "":
            return f'''
<div class="grid cards" markdown><div class="grid-item" style="text-align: center; width: 20%;" markdown>
    
[![{title}]({img_path}){{.small-icon}}]({mdlink})
    
</div><div class="grid-item" style="text-align: left; width: 70%;" markdown>
    
#### [{title}]({mdlink})

Tác Giả: __{author}__

{description}

</div>
</div>
'''
        else:
            return f'''
<div class="grid cards" markdown><div class="grid-item" style="text-align: center; width: 20%;" markdown>
    
![{title}]({img_path}){{.small-icon}}
    
</div><div class="grid-item" style="text-align: left; width: 70%;" markdown>
    
#### {title}

Tác Giả: __{author}__

{description}

</div>
</div>
'''