import os
import binascii
from fabric.api import run, env, task

PROJECT = 'grafana-stack'
GRAFANA_PORT = 3000

if not env.hosts:
    env.hosts = ['pg.remote']


def get_evars(e):
    return ' '.join(f'-e "{k}={v}"' for k, v in e.items() if v)


@task
def init():
    """Prepares directory structure and docker network on a remote host"""
    run(f'''
        mkdir -p ~/{PROJECT}/data/carbon ~/{PROJECT}/data/grafana
        docker network inspect {PROJECT} > /dev/null || docker network create {PROJECT}
        docker pull baverman/graphite
        docker pull baverman/grafana
    ''')


@task
def restart_graphite():
    """Restarts graphite service"""
    run(f'''
        docker stop -t 10 graphite
        docker rm graphite || true
        cd {PROJECT}
        docker run -d --name graphite -p 2003:2003 --restart always --network {PROJECT} \\
                   -v $PWD/data/carbon:/data -u $UID:$GROUPS \\
                   baverman/graphite
        sleep 10
        docker logs --tail 10 graphite
    ''')


@task
def restart_grafana():
    """Restarts grafana service"""
    secret_key = binascii.hexlify(os.urandom(20)).decode()
    evars = get_evars({'GF_SERVER_DOMAIN': env.host,
                       'GF_SERVER_ROOT_URL': f'http://{env.host}:3000/',
                       'GF_SECURITY_SECRET_KEY': secret_key})
    run(f'''
        docker stop -t 10 grafana
        docker rm grafana || true
        cd {PROJECT}
        docker run -d --name grafana -p 3000:3000 {evars} --restart always --network {PROJECT} \\
                   -v $PWD/data/grafana:/data -u $UID:$GROUPS \\
                   baverman/grafana
        sleep 3
        docker logs --tail 10 grafana
    ''')
