from drh.drh import DIPRequestHandler
from rv.rv import RequestViewer

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
# info.printresponse()
#
# uc0 = {
#     "vzePath": None,
#     "profileNo": 0,
#     "deliveryType": "download",
#     "outputPath": "testoutput",
#     "chosenAips": [
#         "Tarfiles/ab7e4f2b-edd2-45d9-8fdc-49d0431bfb1b.tar",
#         "Tarfiles/d3638f0c-82a7-2a3b-afcd-a10c4057e845.tar"
#     ]
# }
#
# uc1 = {
#     "vzePath": None,
#     "profileNo": 1,
#     "deliveryType": "viewer",
#     "outputPath": "testoutput",
#     "chosenAips": [
#         "Tarfiles/d3638f0c-82a7-2a3b-afcd-a10c4057e845.tar"
#     ]
# }
#
# # uc2 = {
# #     "vzePath": None,
# #     "profileNo": 2,
# #     "deliveryType": "both",
# #     "outputPath": "testoutput",
# #     "chosenAips": [
# #         "Tarfiles/ab7e4f2b-edd2-45d9-8fdc-49d0431bfb1b.tar",
# #         "Tarfiles/d3638f0c-82a7-2a3b-afcd-a10c4057e845.tar"
# #     ]
# # }
#
uc3 = {
    "vzePath": None,
    "profileNo": 3,
    "deliveryType": "download",
    "outputPath": "testoutput",
    "chosenAips": [
        "Tarfiles/d3638f0c-82a7-2a3b-afcd-a10c4057e845.tar"
    ]
}
#
# req = drh.startrequest(uc0)
# print()
# print("Request 0:")
# req.printresponse()
#
# req = drh.startrequest(uc1)
# print()
# print("Request 1:")
# req.printresponse()
#
# # req = drh.startrequest(uc2)
# # print()
# # print("Request 2:")
# # req.printresponse()
#
# req1 = drh.startrequest(uc3)
# print()
# print("Request 3.1:")
# req1.printresponse()
# #
# req2 = drh.startrequest(uc3)
# print()
# print("Request 3.2:")
# req2.printresponse()

rv = RequestViewer(drh)
