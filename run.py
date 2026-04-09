from atut_serv import start_serv
from util.svlog import logs

ver = "2026-04-09 21:23:03"
ts = 1775740983
if __name__ == '__main__':
    logs.logger.info(f'下载转发端主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
