from flask import render_template, request, Blueprint
from app.models import Post

main = Blueprint('main', __name__)


@main.route('/', methods=['GET','POST'])
def index():
    # posts = Post.query.all()
    page = request.args.get('page', type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template ('index.html',judul='Home', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html', judul='About')