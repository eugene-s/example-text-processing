from celery import current_app as app


@app.task
def text_embeddings(article_id):
    pass
