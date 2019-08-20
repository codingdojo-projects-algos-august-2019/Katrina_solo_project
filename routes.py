from config import app
from controller import index, edit

app.add_url_rule("/", view_func=index)
app.add_url_rule("/edit", view_func=edit, methods=['POST'])

