from drh.drh import DIPRequestHandler

confPath = "config/DIP/"
confName = "profile_conf.json"

drh = DIPRequestHandler(confPath, confName)

# Todo: absolute paths
# aips = [
#     "\\Projects\\DIPGenerator\\Tarfiles\\ab7e4f2b-edd2-45d9-8fdc-49d0431bfb1b.tar",
#     "\\Projects\\DIPGenerator\\Tarfiles\\d3638f0c-82a7-2a3b-afcd-a10c4057e845.tar"
# ]
aips = [
    "Tarfiles/ab7e4f2b-edd2-45d9-8fdc-49d0431bfb1b.tar",
    "Tarfiles/d3638f0c-82a7-2a3b-afcd-a10c4057e845.tar"
]
# aips = "Tarfiles"

drh.parse_aip(aips)
