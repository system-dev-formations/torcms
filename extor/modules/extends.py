# -*- coding:utf-8 -*-

import tornado.web



import datetime
from torcms.model.post_model import MPost
import tornado.escape
from torcms.core import tools
from torcms.model.core_tab import TabReply
from torcms.model.core_tab import TabUser2Reply
from torcms.model.wiki_model import MWiki
from torcms.model.abc_model import Mabc
from torcms.model.category_model import MCategory
from torcms.model.collect_model import MCollect

import config

class index_post(tornado.web.UIModule):
    '''
    return the post of recent.
    '''

    def render(self, num=10, with_catalog=True, with_date=True, kind='1'):
        kwd = {
            'with_date': with_date,
            'with_catalog': with_catalog,
            'router': config.router_post['1'],
            'kind': kind
        }
        return self.render_string('modules_ext/index_post.html',
                                  recs=MPost.query_recent(num, kind=kind),

                                  kwd=kwd)