import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))
def delete_entry(title):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
def parseHtml(markup):
    p=re.compile(r"######(.+)")
    markup=p.sub(r"<h6>\1</h6>",markup)
    p=re.compile(r"#####(.+)")
    markup=p.sub(r"<h5>\1</h5>",markup)
    p=re.compile(r"####(.+)")
    markup=p.sub(r"<h4>\1</h4>",markup)
    p=re.compile(r"###(.+)")
    markup=p.sub(r"<h3>\1</h3>",markup)
    p=re.compile(r"##(.+)")
    markup=p.sub(r"<h2>\1</h2>",markup)
    p=re.compile(r"#(.+)")
    markup=p.sub(r"<h1>\1</h1>",markup)
    p=re.compile(r"\*\*([a-zA-Z0-9\s.-]+)\*\*")
    markup=p.sub(r"<strong>\1</strong>",markup)
    print(markup)
    p=re.compile(r"\*(\S)*")
    markup=p.sub(r"<li>\1</li>",markup)
    p=re.compile(r"\[([a-zA-Z0-9\s/.-]+)\]\(([a-zA-Z0-9\s/.-]+)\)")
    markup=p.sub(r"<a href=\2 >\1</a>",markup)
    
    return markup
def Search(term):
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.upper().find(term.upper())!=-1))    