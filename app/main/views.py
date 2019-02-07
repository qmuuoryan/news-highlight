#from flask import render_template
#from app import app


@app.route('/News/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news page and its data
    '''
    return render_template('news.html',id = news_id)