# flake8: noqa
from .cli import main

# TODO: the following imports can be removed when we drop the `rqinfo` and
# `rqworkers` commands in favor of just shipping the `rq` command.
from .cli import info
