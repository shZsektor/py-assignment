import sys
import time
from index import Index
from bottle import route, run, template, request
from prometheus_client import start_http_server


if __name__ == '__main__':
    index = Index.new(sys.argv[1])

    @route('/')
    def search():
        q = request.query.q
        print(q, type(q))
        return dict(results=list(index.search(str(q))))

    #time.sleep(120) #Atrifical sleep time to simulate delay in start up to test with kubernetes
    start_http_server(8000)
    run(host=sys.argv[2])
