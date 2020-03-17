import urllib3

def test_homepage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/')
    assert 200 == r.status

def test_battlespage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/battles')
    assert 200 == r.status

def test_updateGpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/update/commander')
    assert 200 == r.status

def test_updateBpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/update/battle')
    assert 200 == r.status

def test_relationspage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.9.150:5000/event')
    assert 200 == r.status

#def test_ghostpage():
#    http = urllib3.PoolManager()
 #   r = http.request('GET','http://35.246.9.150:5000/ghost')
 #   assert 200 == r.status