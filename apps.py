from suit.apps import DjangoSuitConfig
from suit.menu import ChildItem, ParentItem



class SuitConfig(DjangoSuitConfig):
    # layout = 'vertical'
    form_inlines_hide_original = True
    menu = (
        ParentItem('Catalog', children=[
            ChildItem(model='catalog.product'),
        ], icon='fa fa-leaf'),
        ParentItem('Language', children=[
            ChildItem(model='lang.language'),
            ChildItem(model='lang.keyword'),
            ChildItem(model='lang.translation'),
        ]),
        ParentItem('Users', children=[
            ChildItem(model='auth.user'),
            ChildItem('User groups', 'auth.group'),
        ], icon='fa fa-users'),
    )
