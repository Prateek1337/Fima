import rbac.acl
# create access control list
acl = rbac.acl.Registry()

# add roles
acl.add_role("viewer")
acl.add_role("user", ["viewer"])

# add resources
acl.add_resource("register")
acl.add_resource("user_login")
acl.add_resource("user_search")
acl.add_resource("make_transaction")
acl.add_resource("user_profile_view")
acl.add_resource("user_profile")
acl.add_resource("show_notification")
acl.add_resource("delete_account")
acl.add_resource("add_notification")
acl.add_resource("move_notification")
acl.add_resource("logout")

# set rules
acl.allow("viewer", "access", "register")
acl.allow("viewer", "access", "user_login")
acl.allow("user","access","user_search")
acl.allow("user","access","make_transaction")
acl.allow("user","access","user_profile_view")
acl.allow("user","access","user_profile")
acl.allow("user","access","show_notification")
acl.allow("user","access","delete_account")
acl.allow("user","access","add_notification")
acl.allow("user","access","move_notification")
acl.allow("user","access","logout")

if(__name__=="__main__"):
    # use acl to check permission
    if acl.is_allowed("viewer", "access", "register"):
        print("Viewer can access register.")
    else:
        print("Viewer cannnot access register.")

    # use acl to check permission
    if acl.is_allowed("viewer", "access", "user_search"):
        print("Viewer can access user_search.")
    else:
        print("Viewer cannnot access user_search.")

    # use acl to check permission again
    if acl.is_allowed("user", "access", "user_search"):
        print("user can access user_search.")
    else:
        print("user cannnot access user_search.")