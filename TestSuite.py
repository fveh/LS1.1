import unittest
from LibertyShield_v4.1 import UDPEnhancements, ProxyChainScheduler

class TestUDPEnhancements(unittest.TestCase):
    def test_protocol_signatures(self):
        self.assertIn('dns', UDPEnhancements.PROTOCOL_SIGNATURES)
        self.assertGreater(len(UDPEnhancements.PROTOCOL_SIGNATURES['dns']), 8)

class TestProxyScheduler(unittest.TestCase):
    def test_rotation_pattern(self):
        proxies = ['p1', 'p2', 'p3', 'p4', 'p5']
        scheduler = ProxyChainScheduler(proxies)
        self.assertEqual(scheduler.get_next_proxy(), 'p1')
        self.assertEqual(scheduler.get_next_proxy(), 'p4')
        self.assertEqual(scheduler.get_next_proxy(), 'p2')

if __name__ == '__main__':
    unittest.main()
