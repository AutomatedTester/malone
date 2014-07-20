import re

from mercurial import commands

import bugsy


def malone(ui, repo, node, **opts):
    user = ui.config('ui', 'username')
    user = re.search(r'<(.*)>', user).group(1)
    if user:
        password = ui.prompt("Please enter in your password so we can access bugzilla for you", default=None)
        if password:
            bugzilla = bugsy.Bugsy(user, password)
        else:
            ui.write("Accessing Bugzilla without credentials, this may limit what bugs we download")
            bugzilla = bugsy.Bugsy()

        bugs = bugzilla.search_for\
                       .assigned_to(user)\
                       .search()
        working_on = {'bugs': []}
        for bug in bugs:
            working_on['bugs'].append(bug.to_dict())

    else:
        ui.write('Please make sure that you have added your user name to your .hgrc')

cmdtable = {
    "malone": ( malone,
            [("g", "get", "", "Get all bugs assigned to you")],
            "Keep all your bugs with you so you can keep on working without internet"
        )
}