import conf
from minio import Minio
from minio.error import ResponseError

class Operation:
    client = None
    def __init__(self):
        minio_conf = conf.Conf()
        self.client = Minio(minio_conf.get_endpoint(), access_key=minio_conf.get_access_key(), secret_key=minio_conf.get_secret_key(),secure=minio_conf.get_secure())

    def make_bucket(self,bucket_name):
        try:
            self.client.make_bucket(bucket_name=bucket_name)
        except ResponseError as err:
            print err
            exit(0)
        print "cminio: create [%s] bucket success" % bucket_name
    def list_buckets(self):
        buckets = self.client.list_buckets()
        print '[bucket name]\t','[create time]\t'
        for bucket in buckets:
            print '%s\t%s\t' % (bucket.name, bucket.creation_date)
    def bucket_exists(self,bucket_name):
        try:
            if self.client.bucket_exists(bucket_name=bucket_name):
                print "cminio: the [%s] bucket is exist" % bucket_name
            else:
                print "cminio: the [%s] bucket is not exist" % bucket_name
        except ResponseError as err:
            print err

    def list_objects(self,prefix,bucket_name,recursive):
        objects = self.client.list_objects(bucket_name=bucket_name,prefix=prefix,recursive=recursive)
        print "[bucket name]\t[object name]\t[object last modified]\t[etag]\t[size]\t[content type]\t"
        i = 0
        for object in objects:
            print "%s\t%s\t%s\t%s\t%s\t%s\t" % (object.bucket_name,object.object_name.encode('utf-8'),object.last_modified,object.etag,object.size,object.content_type)
            i = i + 1
        print "\n Total: %s object[s]" % i

    def get_bucket_policy(self,bucket_name):
        policy = self.client.get_bucket_policy(bucket_name=bucket_name)
        print "cminio: %" % policy
    def set_bucket_policy(self,bucket_name,policy):
        print ""

    def get_bucket_notification(self,bucket_name):
        notification = self.client.get_bucket_notification(bucket_name=bucket_name)
        print "cminio: %s" % notification

