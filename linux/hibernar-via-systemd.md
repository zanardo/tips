# Hibernar computador via systemd

Para hibernar o computador via *systemd*:

```bash
sudo systemctl hibernate
```

É necessário ter uma partição *swap* com tamanho suficiente para conter o
conteúdo da memória *RAM*.

Alternativamente, é possível suspender o computador e também gravar o conteúdo
da memória *RAM* na *swap* para ser utilizado caso o computador desligue (ex:
bateria acabando, falta de energia):

```bash
sudo systemctl hybrid-sleep
```

Isto é útil para ligar o computador rapidamente, e manter em baixo consumo de
energia.
