from atut_serv import start_serv
from util.svlog import logs

ver = "2026-04-16 23:17:02"
ts = 1776352622
if __name__ == '__main__':
    logs.logger.info(f'下载转发端主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
