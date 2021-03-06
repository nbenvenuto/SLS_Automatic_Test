import os
import sys
import subprocess


class ClusterInteraction():

  def __init__(self, ci_path):
    self.ci_path = ci_path
    
  def discovery(self):
    cmd = ['discovery']
    return self.sendCmd(cmd)
    
  def fwUpdate(images):
    pass
      
  def ptsUpdate(self):
    pass
    
  def setProductionMode(self):
    pass
    
  def setSerialNumber(self, production_mode):
    pass
    
  def setPartNumber(self, production_mode):
    pass
    
  def setMGPartNumber(self, production_mode):
    pass
      
  def mibUpdate(self):
    pass
    
  def buildImages(self):
    pass
    
  def enableZoneSetSwith(self):
    cmd = ['zoneset-lock']
    return self.sendCmd(cmd)

  def disableZoneSetSwith(self):
    cmd = ['zoneset-unlock']
    return self.sendCmd(cmd)
    
  def changeZoneSet(self, zone_ix):
    cmd = ['zoneset-select', 'idx={}'.format(zone_ix)]
    return self.sendCmd(cmd)
 
  def sendCmd(self, cmd):
    full_cmd = [self.ci_path, '--consoleMode', '-k']
    full_cmd.extend(cmd)
    
    try:
      with open(r'C:\test.txt', 'w') as fout:
        subprocess.run(full_cmd, stdout=fout)
    except subprocess.CalledProcessError:
      print('Command failed.')
      exit(1)
      
    tmp_file = r'C:\test.txt'
    with open(tmp_file, 'r') as fout:
      data = fout.read()
    os.remove(tmp_file)
    
    return data


def main():
  ci_path = r'C:\Program Files (x86)\Datalogic\DLSentinel\3.1.0\DLSentinel.exe'
  ci = ClusterInteraction(ci_path)
  output = ci.discovery()
  output = ci.enableZoneSetSwith()


  try:
    while True:
      zone_set = input('Please enter a zone set (CTRL+C to exit): ')
      output = ci.changeZoneSet(zone_set)
      print('Zone set changed to {}'.format(zone_set))
  except KeyboardInterrupt:
    ci.disableZoneSetSwith()
    print('Exit!')
    sys.exit(0)


if __name__ == '__main__':
  main()