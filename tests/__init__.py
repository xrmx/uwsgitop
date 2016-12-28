import os
import subprocess
import tempfile
import time
import unittest


UWSGI =  os.environ.get('UWSGI_BIN', 'uwsgi')


class TestUwsgitop(unittest.TestCase):
    def setUp(self):
        self.stdin = open(os.devnull, 'r')
        self.stdout = open(os.devnull, 'w')
        self.stderr = tempfile.TemporaryFile()

        self.commands = []

    def tearDown(self):
        self.stdin.close()
        self.stdout.close()
        self.stderr.close()
        self.terminate_cmd(self.commands)

    def run_cmd(self, command, wait=0):
        cmd = subprocess.Popen(
            command,
            close_fds=True,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        if wait:
            time.sleep(wait)
        self.commands.append(cmd)
        return cmd

    def terminate_cmd(self, commands):
        for cmd in commands:
            cmd.terminate()
        for cmd in commands:
            cmd.wait()

    def test_read_from_unix_socket(self):
        uwsgi = self.run_cmd(
            [UWSGI, '--http', ':0', '--stats', '/tmp/stats.socket', '--logto', '/dev/null']
        )
        uwsgitop = self.run_cmd(['python', 'uwsgitop', '/tmp/stats.socket'], wait=1)
        self.assertEqual(self.stderr.tell(), 0)

    def test_read_from_socket(self):
        uwsgi = self.run_cmd(
            [UWSGI, '--http', ':0', '--stats', ':3031', '--logto', '/dev/null']
        )
        uwsgitop = self.run_cmd(['python', 'uwsgitop', ':3031'], wait=1)
        self.assertEqual(self.stderr.tell(), 0)

    def test_read_from_http(self):
        uwsgi = self.run_cmd(
            [UWSGI, '--http', ':0', '--stats', ':3031', '--stats-http', '--logto', '/dev/null']
        )
        uwsgitop = self.run_cmd(['python', 'uwsgitop', 'http://0.0.0.0:3031'], wait=1)
        self.assertEqual(self.stderr.tell(), 0)


if __name__ == '__main__':
    unittest.main()
