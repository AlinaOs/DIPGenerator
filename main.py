from drh.drh import DIPRequestHandler
from rv.gui import RequestViewer

confdir = "config/DIP/"
conf = "profile_conf.json"
vconfdir = "config/VDIP/"
vconf = "profile_conf.json"

drh = DIPRequestHandler(confdir, conf, vconfdir, vconf)

# Single AIP absolute paths
# aips = [
#     "C:/Projects/DIPGenerator/Tarfiles/ab7e4f2b-edd2-45d9-8fdc-49d0431bfb1b.tar",
#     "C:/Projects/DIPGenerator/Tarfiles/d3638f0c-82a7-2a3b-afcd-a10c4057e845.tar"
# ]

# Single AIP relative paths
aips = [
    "Tarfiles/ab7e4f2b-edd2-45d9-8fdc-49d0431bfb1b.tar",
    "Tarfiles/d3638f0c-82a7-2a3b-afcd-a10c4057e845.tar",
    "Tarfiles/d3638f0c-82a7-2a3b-afcd-a10c4057e845.tar"
]

# AIPs in a dir
# aips = "Tarfiles"

# info = drh.getaipinfo(aips)
#
# print("AIP-Info:")
# print(info["aipinfo"])
# print("VZE-Info:")
# print(info["vzeinfo"])

uc = {
    "aipPaths": aips,
    "vzePath": None,
    "profileNo": 0,
    "deliveryType": "both",
    "outputPath": "testoutput",
    "chosenAips": ["d3638f0c-82a7-2a3b-afcd-a10c4057e845", "ab7e4f2b-edd2-45d9-8fdc-49d0431bfb1b"]
}

req = drh.startrequest(uc)

# rv = RequestViewer()
