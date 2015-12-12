import urllib.request
# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "https://jira.realeyesit.com/bamboo/rest/api/latest/result.json"
password_mgr.add_password(None, top_level_url, 'zoltan.gomori', 'Suf214gsh3016')

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
# opener.open(top_level_url)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

with urllib.request.urlopen('https://jira.realeyesit.com/bamboo/rest/api/latest/result.json?os_authType=basic') as response:
   html = response.read()

print(html)