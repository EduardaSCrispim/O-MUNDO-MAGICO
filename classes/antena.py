class Antena:

    def __init__(self, id_antena, bytes_sent, bytes_recv,
                 active_conn, cpu_usage, ram_usage, timestamp):

        self.id_antena = id_antena
        self.bytes_sent = bytes_sent
        self.bytes_recv = bytes_recv
        self.active_conn = active_conn
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.timestamp = timestamp