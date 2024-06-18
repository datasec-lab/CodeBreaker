from flask import (Blueprint, g, render_template, url_for)
import jinja2 as j2
bp = Blueprint('adm', __name__, url_prefix='/adm')

@bp.route('/')
def index():
   with open('adm/index.html') as f:
       create_template = lambda x: j2.Template(x)
       return create_template(f.read()).render()