from mercurial import commands

def malone():
    pass

cmdtable = {
    "malone": ( malone,
            [("g", "get", "", "Get all bugs assigned to you")],
            "Keep all your bugs with you so you can keep on working without internet"
        )
}