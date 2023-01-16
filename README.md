# mspl_ee602-2_server_docker
mspl_ee602-2_server_docker
用力瑋資料夾的dockerfile為基礎編輯的
用於EE602-2的Server6上
此版本相較於mspl:cuda11.1-cudnn8-tf2.3-keras-torch1.8-py3-gpu
- 改進了進終端不用打bash
- 增加清華的鏡像這樣下apt-get upgrade才不會卡卡的
- python版本安裝

#:heart::kissing_heart::ok_hand::sweat_drops::imp: Docker 規則 :heart::kissing_heart::ok_hand::sweat_drops::imp:
#### :imp:所有Docker 要掛載在/data下:imp:
#### :imp:所有Docker port依序建立，jupyterlab跟tensorboard port 皆是90XX, 60XX, XX都一樣:imp:

------------


```
docker images : 顯示所有docker images
docker rmi $docker_id : 刪除build的images
docker ps -a | grep 90 : 顯示容器
docker stop $NAME : 容器中止
docker rm $NAME : 容器刪除
```

------------


Docker Build 指令

- sudo docker build -t $REPOSITORY:$TAG . --no-cache 需要cd到Dockerfile的目錄

Example: 
```
sudo docker build -t lian_docker_4th_test:py37 . --no-cache
```

------------


Docker Run 指令

- -v 掛載位置 : 要先在/data裡面先建立好
- -p port 轉送 : 9033:8888 **jupyterlab** 6033:6006 **tensorboard** port號不能重複!
- --name 容器名稱

Example: 
```
NV_GPU=0,1,2,3 nvidia-docker run -it -d -v /data/lian_dockertest2/:/workspace -p 9033:8888 -p 6033:6006 --name lian_dockertest-9033 lian_docker_4th_test:py37
```

------------


Docker 獲取token 指令
Example: 
```
docker logs lian_dockertest-9033 | grep token
```