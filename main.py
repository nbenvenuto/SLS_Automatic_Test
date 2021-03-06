import sys
import ClusterInteractionClass as ciClass

ci_path = r'C:\Program Files (x86)\Datalogic\DLSentinel\3.1.0\DLSentinel.exe'


def ci_process():
    ci = ciClass.ClusterInteraction(ci_path)
    output = ci.discovery()
    output = ci.enable_zone_sets_swith()

    try:
        while True:
            zone_set = input('Please enter a zone set (CTRL+C to exit): ')
            output = ci.change_zone_set(zone_set)
            print('Zone set changed to {}'.format(zone_set))
    except KeyboardInterrupt:
        ci.disable_zone_sets_swith()
        print('Exit!')
        sys.exit(0)


def ci_set_status():
    ci = ciClass.ClusterInteraction(ci_path)
    ci.discovery()

    try:
        while True:
            value_status = input('Please enter a zone set (CTRL+C to exit): ')
            ci.set_status(value_status)
            print(f'Status changed to {value_status}')
    except KeyboardInterrupt:
        ci.disable_zone_sets_swith()
        print('Exit!')
        sys.exit(0)


def ci_insert_fault():
    ci = ciClass.ClusterInteraction(ci_path)
    ci.discovery()
    try:
        while True:
            fault = input('Please enter fault (CTRL+C to exit): ')
            dst = input('Please enter dst (CTRL+C to exit): ')
            ci.insert_fault(fault, dst)
    except KeyboardInterrupt:
        print('Exit!')
        sys.exit(0)


ci_set_status()
