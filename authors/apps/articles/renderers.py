
from ..renderers import MainRenderer


class CategoryJSONRenderer(MainRenderer):
    object_label = 'category'


class ArticleJSONRenderer(MainRenderer):
    object_label = 'article'


class BookmarkJSONRenderer(MainRenderer):
    object_label = 'bookmark'


class TagJSONRenderer(MainRenderer):
    object_label = 'tag'


class CommentHistoryJSONRenderer(MainRenderer):
    object_label = 'history'
