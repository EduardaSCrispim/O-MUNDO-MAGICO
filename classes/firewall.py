class Firewall:

    def __init__(self, active_sessions, dropped_packets,
                 top_blocked_ip, cpu_usage, ram_usage,
                 bytes_sent, bytes_recv, timestamp):

        self.active_sessions = active_sessions
        self.dropped_packets = dropped_packets
        self.top_blocked_ip = top_blocked_ip
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.bytes_sent = bytes_sent
        self.bytes_recv = bytes_recv
        self.timestamp = timestamp