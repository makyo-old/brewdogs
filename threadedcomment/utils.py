from brewdogs.threadedcomment.models import *
from django.contrib.contenttypes.models import ContentType

def comments_for_object(o):
    ct = ContentType.objects.get_for_model(o.__class__)
    comments = Comment.objects.filter(topic_type__id__eq = ct.id, topic_id__eq = o.id)
    tree = []
    for comment in comments:
        _build_tree(tree, comment)
    return tree

def _build_tree(tree, comment):
    if comment.parent:
        for leaf in tree:
            if comment.parent == leaf['comment']:
                leaf['subcomments'].append({'comment': comment, 'subcomments': []})
            else:
                if len(leaf['subcomments']) > 0:
                    _build_tree(leaf['subcomments'])
    else:
        tree.append({'comment': comment, 'subcomments': []})
