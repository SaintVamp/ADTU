from atut_serv import start_serv
from util.svlog import logs

ver = "2026-01-15 21:36:04"
ts = 1768484164
if __name__ == '__main__':
    logs.logger.info(f'下载转发端主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
