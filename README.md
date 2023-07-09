# BannerServer

これは文字列を大きな文字で返してくれるWebアプリケーションです。

## 使用例

```bash
curl http://127.0.0.1:5000/HelloWorld!
```

```text
 _   _      _ _    __        __         _     _ _ 
| | | | ___| | | __\ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/ \_/\_/ \___/|_|  |_|\__,_(_)
```

banner文字列であれば、カタカナもいけます。

```bash
curl http://127.0.0.1:5000/banner/コンニチワ
```

```text
                   #                   ##  ########## 
########## #       #             ######    #        # 
         #  #     #    ######        #             #  
         #       #              ##########        #   
         #     ##                    #           #    
         #   ##      ##########      #         ##     
#########  ##                      ##        ##       
```

# Dockerイメージを作って動かしてみる

Dockerイメージを作るには:

```bash
cd BannerServer/
docker build -t banner-server:0.1 .
```

Dockerイメージを起動するには:

```bash
docker run -it -p 15000:5000 --name banner banner-server:0.1
```

デーモンで起動するには:

```bash
docker run -d --restart always -p 15000:5000 --name banner banner-server:0.1
```

ホスト側のポート番号を15000に変更しているので、URLは以下のようになる。


```bash
curl http://127.0.0.1:15000/HelloWorld!
```
