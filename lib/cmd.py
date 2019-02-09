# the console command.
import argparse
from lib import operation
class Command:

    def __init__(self):
        parser = argparse.ArgumentParser(description='A command minio tools. Version:1.0.')
        parser.add_argument("-m","--makebucket",help="create a new bucket.")
        parser.add_argument("-l","--listbuckets",help="list the all buckets",action="store_true")
        parser.add_argument("-e","--bucketexists",help="the bucket if exists")
        parser.add_argument("-r",'--removebucket',help="remove the buckets")
        parser.add_argument("--listobjects",help="list the all objects")
        parser.add_argument("--getbucketpolicy",help="get bucket policy")
        parser.add_argument("--setbucketpolicy", help="set bucket policy")
        parser.add_argument("--getbucketnotification", help="get bucket notification")
        args = parser.parse_args()

        cminio_operation = operation.Operation()


        if args.makebucket:
            cminio_operation.make_bucket(args.makebucket)
        elif args.listbuckets:
            cminio_operation.list_buckets()
        elif args.bucketexists:
            cminio_operation.bucket_exists(args.bucketexists)
        elif args.listobjects:
            prefix = raw_input('the prefix of objects that should be listed(None):')
            recursive = raw_input("(Y) indicates recursive style listing and (N) indicates directory listing delimited by '/'(Y/N):")
            while recursive != 'Y' and recursive != 'N':
                recursive = raw_input(
                    "(Y) indicates recursive style listing and (N) indicates directory listing delimited by '/'(Y/N):")
            prefix_x = None if (prefix == '')  else prefix
            recursive_e = True if (recursive == 'Y') else False
            cminio_operation.list_objects(prefix=prefix_x, bucket_name=args.listobjects,recursive=recursive_e)
        elif args.getbucketpolicy:
            cminio_operation.get_bucket_policy(args.getbucketpolicy)
        elif args.setbucketpolicy:
            #cminio_operation.set_bucket_policy(args.setbucketpolicy)
            print ""
        elif args.getbucketnotification:
            cminio_operation.get_bucket_notification(args.getbucketnotification)