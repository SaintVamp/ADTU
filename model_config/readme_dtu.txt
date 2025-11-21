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
三、修改config中config.toml中的内容。
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
五、QB容器映射的资源地址和DTU容器映射的资源地址必须一致！！！

Q&A：
Q1：config里的model-config.toml是干什么的？
A1：这个是最全的配置文件模版。在第一次创建容器后，需要复制model-config.toml一份并改名为config.toml，然后配置config中的必备信息。
另外每次更新model后，重启时程序会自动更新model-config.toml，并将config.toml缺少的配置项补全，但仍需要人工配置此类配置项的值。

Q2：当前支持哪些源站，哪些目标站？
A2：源站支持【观众、季节、憨憨、家园、杜比、HDV、朋友、猫、织梦、优堡、reelflix、FL】
目标站支持【末日、象岛、优堡、麒麟、劳改所、织梦、柠檬、南工大】

Q3：如何限制指定内容禁转。
A3：在forbidden文件夹中配置对应站点的禁转内容。


API说明：
PS:如果是curl命令要把调用方法整体引号引起，浏览器则无影响。
如：curl "http://127.0.0.1:45678/sv/dtu/api/getHashInfo?h=123123qazwsxedcqwe123"

1.强制获取RSS数据接口：forceRss
功能：立刻拉取RSS队列中的种子资源，加入到DTU下载发布
调用方法：http://127.0.0.1:45678/sv/dtu/api/forceRss

2.获取源种存储信息接口：getHashInfo
功能：查看源种存储内容是否正确，主要修复BUG用
调用方法：http://127.0.0.1:45678/sv/dtu/api/getHashInfo?h={QB种子信息中的信息哈希值}

3.哈希值删除发布任务接口：delTorrent
功能：用哈希值查询并删除相关的发布任务
调用方法：http://127.0.0.1:45678/sv/dtu/api/delTorrent?h={QB种子信息中的信息哈希值}

4.源种现在完成通知接口：downloaded
功能：接受下载工具的通知消息，也可人工调用
调用方法：http://127.0.0.1:45678/sv/dtu/api/downloaded?h={QB种子信息中的信息哈希值}

5.目标站重发接口：reload
功能：用于对已下载好的种子通知重发指定目标站
调用方法：http://127.0.0.1:45678/sv/dtu/api/reload?h={QB种子信息中的信息哈希值}&ts={目标站点域名}
目标站点域名：可在config.toml文件中的domain配置项中查看

6.源站种子重发接口：reloadAll
功能：用于对已下载好的种子通知重发所有目标站
调用方法：http://127.0.0.1:45678/sv/dtu/api/reloadAll?h={QB种子信息中的信息哈希值}

7.查询未完成任务接口：unfinished
功能：查询任务库中未完成下载的任务，用于检查是否源种下载失败
调用方法：http://127.0.0.1:45678/sv/dtu/api/unfinished
