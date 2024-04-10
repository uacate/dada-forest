apt install -y debian-keyring debian-archive-keyring apt-transport-https -y
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
apt-get update -y
apt-get install caddy -y
systemctl enable --now caddy
mkdir -p /var/www/html 

cat > /var/www/html/index.html <<EOF
<html>
   <head>
      <title>DADA-Forest</title>
   </head>
</html>
EOF


# When A record is setup replace ":80" with domain name
cat > /etc/caddy/Caddyfile <<EOF
dadaforest.net {
    root * /var/www/html/

    # Enable static file server
    file_server

    # Setup reverse proxy
    # reverse_proxy localhost:8000 {
    #    header_down Strict-Transport-Security max-age=31536000;
    # }
}
EOF

#!/usr/bin/bash
export DEBIAN_FRONTEND=noninteractive
