☆☆☆所有命令请复制【】中全部内容。所有{}请替换为本机展现内容☆☆☆
☆☆☆所有命令请复制【】中全部内容。所有{}请替换为本机展现内容☆☆☆
☆☆☆所有命令请复制【】中全部内容。所有{}请替换为本机展现内容☆☆☆

一、拉取镜像：【docker pull saintvamp/auto_dtu:latest】
二、创建容器：【docker run -d --network host \
--name=auto_dtu \
-e TZ=Asia/Shanghai \
-v /{DTU的父目录地址}/auto_dtu/bdinfo:/auto_dtu/bdinfo \
-v /{DTU的父目录地址}/auto_dtu/config:/auto_dtu/config \
-v /{DTU的父目录地址}/auto_dtu/database:/auto_dtu/database \
-v /{DTU的父目录地址}/auto_dtu/forbidden:/auto_dtu/forbidden \
-v /{DTU的父目录地址}/auto_dtu/log:/auto_dtu/log \
-v /{DTU的父目录地址}/auto_dtu/picture:/auto_dtu/picture \
-v /{资源存储的父目录地址}/download:/downloads/disk1 \
saintvamp/auto_dtu:latest】
#自行修改-v中冒号前的文件夹地址后，执行一次，此时程序未运行，只是生成容器。
三、
(1)可以通过访问日志打印的地址(如http://127.0.0.1:45678)进行配置
(2)修改config中config.toml中的内容，配置说明见每个配置项后的说明文字。
四、建议QB使用官方4.6.0或以上版本。创建容器命令：【docker run -d --network host \
--name=qb \
-e PUID=911 \
-e PGID=911 \
-e TZ=Asia/Shanghai \
-e accept \
-v /{QB配置的父目录地址}/config:/config \
-v /{资源存储的父目录地址}/download:/downloads/disk1 \
--restart always \
qbittorrentofficial/qbittorrent-nox:4.6.0-1】
五、QB容器映射的资源地址，DTU容器映射的资源地址，config中配置的地址，三者必须一致！！！

群共享有API调用小工具，可以下载使用。

Q&A：
Q1：config里的model-config.toml是干什么的？
A1：这个是最全的配置文件模版。在第一次创建容器后，需要配置config中的必备信息。
另外每次有model-config.toml的内容更新后，重启时程序会自动更新model-config.toml，并将config.toml缺少的配置项补全，但仍需要人工配置此类配置项的值。

Q2：如何限制指定内容禁转。
A2：在forbidden文件夹中配置对应站点的禁转内容，each_site.toml文件是配置站点间的种子禁转。
