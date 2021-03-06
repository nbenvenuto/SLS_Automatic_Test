import os
import subprocess


class ClusterInteraction:
    def __init__(self, ci_path):
        self.ci_path = ci_path

    def discovery(self):
        cmd = ['discovery']
        return self.sendCmd(cmd)

    def enable_zone_sets_swith(self):
        cmd = ['zoneset-lock']
        return self.sendCmd(cmd)

    def disable_zone_sets_swith(self):
        cmd = ['zoneset-unlock']
        return self.sendCmd(cmd)

    def change_zone_set(self, zone_ix):
        cmd = ['zoneset-select', 'idx={}'.format(zone_ix)]
        return self.sendCmd(cmd)

    def set_status(self, status_value):
        cmd = ['set-status status=', f"{status_value}"]
        return self.sendCmd(cmd)

    def insert_fault(self, fault, dst):
        # cmd = ['insert-fault', 'type={}'.format(fault), 'dst={}'.format(dst)]
        cmd = [f"insert-fault type={fault} dst={dst}"]
        return self.sendCmd(cmd)

    def send_cmd(self, cmd):
        full_cmd = [self.ci_path, '--consoleMode', '-k']
        full_cmd.extend(cmd)

        try:
            with open(r'C:\test.txt', 'w') as function_out:
                subprocess.run(full_cmd, stdout=function_out)
        except subprocess.CalledProcessError:
            print('Command failed.')
            exit(1)

        tmp_file = r'C:\test.txt'
        with open(tmp_file, 'r') as function_out:
            data = function_out.read()
        os.remove(tmp_file)

        return data
