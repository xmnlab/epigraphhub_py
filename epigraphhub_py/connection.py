import atexit

from sshtunnel import SSHTunnelForwarder


class Tunnel:
    def __init__(self):
        self.host = "epigraphhub.org"
        self.server = None
        atexit.register(self.close_tunnel)

    def open_tunnel(self, user="epigraph", ssh_key_passphrase=""):
        """
        Opens a tunnel to EpigraphHub database
        """
        self.server = SSHTunnelForwarder(
            self.host,
            ssh_username=user,
            ssh_password="epigraph",
            ssh_private_key_password=ssh_key_passphrase,
            remote_bind_address=("127.0.0.1", 5432),
        )

        self.server.start()

    def __repr__(self):
        if self.server is None:
            return "Tunnel is closed."
        else:
            return f"Port {self.server.local_bind_port} is being forwarded to {self.host}:5432"

    def close_tunnel(self):
        if not self.server is None:
            print("Closing Tunnel...")
            self.server.stop()
            self.server = None
