from atut_serv import start_serv
from util.svlog import logs

ver = "2026-01-06 04:49:57"
ts = 1767646197
if __name__ == '__main__':
    logs.logger.info(f'下载转发端主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
