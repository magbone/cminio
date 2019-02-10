# create command like shell to connect the server

class Shell:

    shell_cmd = [
        'help',
        'cp',
        'rm',
        'drop',
        'policy'
        'ntf',
        'version'
    ]

    version = '1.0'

    def __init__(self):
        print "Welcome to the cminio shell"
        print "['help','version']"

        while True :
            cmd = raw_input("cminio>")
            self.parser(cmd)
    def parser(self,str):
        arr = str.split()
        if arr[0] not in self.shell_cmd:
            print "Error: No such command: %s" % arr[0]
            return
        else:
            if arr[0] == 'help':
                self.usage()
                return
            elif arr[0] == 'version':
                self.version_print()
                return
            elif arr[0] == 'cp':
                self.copy(arr[1:])
                return
    def usage(self):
        print """
            [help] list the all command map.
            [version] show the cminio version
            [cp] cp the file or object neither from remote to local or from local to remote
            [rm] remove the object
            [drop] delete the bucket
            [policy] set or get policy
            [ntf] set or get notification
        """
    def version_print(self):
        print "cminio version %s" % self.version

    def copy(self,arr):
        copy = {
            'remote': '',
            'local': '',
            'header': '',
            'r2l': False
        }
        for a in arr:
            arr1 = a.split(":")
            if len(arr1) >= 3:
                print "Error: Invalid argument %s" % arr1[2:]
                return
            if len(arr1) == 1 or len(arr1) == 0:
                print "Error: Lack the argument: ':'"
                return
            if arr1[0] == 'r':
                copy['remote'] = arr1[1]
                if copy['local'] == '':
                    copy['r2l'] = True
            elif arr1[0] == 'l':
                copy['local'] = arr1[1]

            elif arr1[0] == 'h':
                copy['header'] = arr1[1]
            else:
                print "Error: No such argument %s" % arr[0]
        if copy['local'] == '':
            print "Error: The 'local' can not be empty"

        if copy['remote'] == '':
            print "Error: The 'remote' can not be empty"

        remote = copy['remote'].split('>')
        if len(remote) >= 3:
            print "Error: Invalid argument %s" % remote[2:]
            return
        if len(remote) == 1 or len(remote) == 0:
            print "Error: Lack the argument: '>'"
            return

        bucket_name = remote[0]
        object_name = remote[1]

        if copy['r2l']:
            #get object
            print "get"
        else:
            #put object
            print "put"