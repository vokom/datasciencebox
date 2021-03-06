import pytest

requests = pytest.importorskip("requests")

import utils


def setup_module(module):
    utils.invoke('install', 'mesos')


@utils.remotetest
def test_salt_formulas():
    project = utils.get_test_project()

    kwargs = {'test': 'true', '--out': 'json', '--out-indent': '-1'}
    out = project.salt('state.sls', args=['cdh5.zookeeper.cluster'], target='head', kwargs=kwargs)
    utils.check_all_true(out, none_is_ok=True)

    kwargs = {'test': 'true', '--out': 'json', '--out-indent': '-1'}
    out = project.salt('state.sls', args=['mesos.cluster'], kwargs=kwargs)
    utils.check_all_true(out, none_is_ok=True)


@utils.remotetest
def test_mesos_ui():
    '''
    Note 1: Mesos UI uses a lot of javascript requests alone is not good enough
    Note 2: Mesos UI does not bing to 0.0.0.0 so need explicit IP if using vagrant 
    '''
    project = utils.get_test_project()
    nn_ip = project.cluster.head.ip

    r = requests.get('http://%s:5050/' % nn_ip)
    assert r.status_code == 200
