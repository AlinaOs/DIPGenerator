"""Main script starting the Request Viewer GUI and initializing the DIP Request Handler."""

from drh.drh import DIPRequestHandler
from rv.rv import RequestViewer

confdir = "config/DIP/"
conf = "profile_conf.json"
vconfdir = "config/VDIP/"
vconf = "profile_conf.json"
texts = "config/guitexts.json"

drh = DIPRequestHandler(confdir, conf, vconfdir, vconf)

rv = RequestViewer(drh, texts)
