from atut_serv import start_serv
from util.svlog import logs

ver = "2025-12-03 21:07:18"
ts = 1764767238
if __name__ == '__main__':
    logs.logger.info(f'下载转发端主程序启动，V1.0.1 ver={ver}')
    start_serv(ts)
