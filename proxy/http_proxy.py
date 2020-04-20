import socket
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import threading

class ProxyServer:
    def __init__(self,host='127.0.0.1',port=1090):
        self.host           = host
        self.port           = port
        self.max_len        = 0xffffff
        self.max_queue      = 0xffffffff
        self.max_thread     = 10
        self.client_sockets = {}
        self.execute    = ThreadPoolExecutor(self.max_thread)
        self.request_queue  = Queue(self.max_queue)
        self.response_queue = Queue(self.max_queue)     
        self.proxy_socket   = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        if self.server_socket != None:
            self.server_socket.bind((host,port))
            self.server_socket.listen()
    
    def client_accept(self):
        while True:
            client_socket,addr = self.server_socket.accept()
            if client_socket  != None:
                key = ':'.join(addr)
                if self.client_sockets[key] == None:
                    self.client_socket[key] = client_socket
                request = client_socket.recv(self.max_len).decode('utf8')
                host,port = addr
                self.worker_queue.put(SendRequest(host,port,request))
        
    def start(self):
        accept = threading.Thread(target=self.client_accept,args=())
        handler = threading.Thread(target=self.handler_worker,args=())
        accept.start()
        handler.start()
        accept.join()
        handler.join()
        # self.execute.submit(self.client_acceot,())
        # self.execute.submit(self.handler_worker,())
        
        
    def get_host(self,request):
        headers,data = request.split('\r\n\r\n')
        for head in headers.split('\r\n'):
            if 'Host:' in head:
                return tuple(head.split(':')[1:])


    def transpond_request(self,req):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host,port = self.get_host(req.request)
        s.connect((host,port))
        s.send(req.request)
        data = s.recv(self.max_len)
        if data != None:
            client = self.client_sockets[req.host+':'+req.port]
            if client != None:
                client.send(data)
            else:
                print('{0} {1} is closed!'.format(req.host,req.port))


    def handler_worker(self):
        while True:
            req = self.request_queue.get()
            self.execute.submit(self,transpond_request,(req,))
class SendRequest:
    def __init__(self,host,port,request):
        self.host = host
        self.port = port
        self.request = request
    
    def keys(self):
        return ('id','name','email')

    def __getitem__(self, item):
        return getattr(self, item)


if __name__ == '__main__':
    proxy = ProxyServer()
    proxy.start()
       
       

