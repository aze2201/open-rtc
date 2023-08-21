# Desktop share as Argument Reality

## Open https://open-rtc.com/display in your browser (better use firefox)
You will QR code and click to share desktop via browser (you can choose any TAB or entire desktop)

## Scan QR code with your mobile
Accept camera, gps and motion request

## wola, you ca connected to desktop

## Here is Apache configuration

### Apache websocket virtual host

```
<IfModule mod_ssl.c>
<VirtualHost *:443>
	
	ServerName open-rtc.com
	Header set Access-Control-Allow-Origin "ws.open-rtc.com"
        Header set Access-Control-Allow-Credentials  "true"
	ProxyPreserveHost On
        
        # Servers to proxy the connection, or;
        # List of application servers:
        # Usage:
        # ProxyPass / http://[IP Addr.]:[port]/
        # ProxyPassReverse / http://[IP Addr.]:[port]/
        # Example: 
	<Location />
		ProxyPass  http://127.0.0.1:8080/
        	ProxyPassReverse  http://127.0.0.1:8080/
        </Location>


	SSLCertificateFile /etc/letsencrypt/live/open-rtc.com/fullchain.pem
	SSLCertificateKeyFile /etc/letsencrypt/live/open-rtc.com/privkey.pem
	Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>
</IfModule>
```

### Here is Apache main web site configuration

```
<VirtualHost *:443>
	
	RewriteEngine on
	Header set Access-Control-Allow-Origin "https://open-rtc.com"
	Header set Access-Control-Allow-Credentials  "true"
        ServerName ws.open-rtc.com

	LoadModule proxy_wstunnel_module        modules/mod_proxy_wstunnel.so

	ProxyPass / http://localhost:8080/
	RewriteEngine on
	RewriteCond %{HTTP:Upgrade} websocket [NC]
	RewriteCond %{HTTP:Connection} upgrade [NC]
	RewriteRule ^/?(.*) "ws://localhost:8080/$1" [P,L]

	SSLCertificateFile /etc/letsencrypt/live/ws.open-rtc.com/fullchain.pem
	SSLCertificateKeyFile /etc/letsencrypt/live/ws.open-rtc.com/privkey.pem
	Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>

```
