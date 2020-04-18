# Obter o IP externo de saída para internet

É possível obter o IP externo de saída para a internet através do DNS usando um
serviço do OpenDNS.

É necessário ter instalado o aplicativo `dig`, no pacote `dnsutils` do Debian:

```bash
apt install dnsutils
```

* Para verificar o IP externo:

```bash
dig +short myip.opendns.com @resolver1.opendns.com
```
