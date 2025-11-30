from atut_serv import start_serv
from util.svlog import logs

ver = "2025-11-30 08:39:41"
ts = 1764463181
if __name__ == '__main__':
    logs.logger.info(f'下载转发端主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
