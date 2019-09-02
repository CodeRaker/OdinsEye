# For adding SSL: https://stackoverflow.com/questions/8582766/adding-ssl-support-to-socketserver

import SocketServer

class RESTServer(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def get_response(self, request_uri):
        if request_uri.lower() == "/nagios":
            return "ClusterMD: Status for Nagios\nStatus: OK!\n"


    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data



        request_uri = self.data.split("\n")[0]
        request_uri = request_uri.split(" ")[1]
        response = self.get_response(request_uri)

        self.request.sendall(response)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
