from python_hosts import Hosts, HostsEntry
import yaml


ENTRIES_FILE_NAME = 'entries.yml'


def add():
    _process(_add_entry)


def clear():
    _process(_remove_entry)


#
def _process(action):
    with open(ENTRIES_FILE_NAME) as entries_file:
        entires = yaml.load(entries_file)

    sys_hosts = Hosts()
    for ip, name in entires:
        action(sys_hosts, ip, name)

    sys_hosts.write()


def _add_entry(hosts, ip, name):
    hosts.add(
        [HostsEntry(entry_type='ipv4', address=ip, names=[name])],
        allow_address_duplication=True,
    )


def _remove_entry(hosts, ip, name):
    hosts.remove_all_matching(name=name)
