def html(tag):
    def f(text):
        return f"<{tag}>{text}</{tag}>"
    return f