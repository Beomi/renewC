# renewC

## Deploy
make deploy.json like this:

```
{
  "REPO_URL": "https://github.com/Beomi/renewC.git",
  "PROJECT_NAME": "renewC",
  "STATIC_ROOT_NAME": "static_deploy",
  "STATIC_URL_NAME": "static",
  "REMOTE_USER": "sudo_granted_user",
  "REMOTE_PW": "some_password",
  "REMOTE_HOST": "your_domain.com",
  "REMOTE_HOST_PORT": "your_server_ssh_port",
  "APT_REQ": [
    "curl",
    "git",
    "python-dev",
    "python3-dev",
    "python3-pip",
    "build-essential",
    "zsh",
    "apache2",
    "libapache2-mod-wsgi-py3",
    "python3-setuptools",
    "ufw"
  ]
}
```
