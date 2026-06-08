from atut_serv import start_serv
from util.svlog import logs

ver = "2026-06-08 11:15:17"
ts = 1780888517
if __name__ == '__main__':
    logs.logger.info(f'下载转发端主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
