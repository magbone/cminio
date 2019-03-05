# cminio

## Prface
A minio command tool

## Usage

```bash
usage: cminio.py [-h] [-m MAKEBUCKET] [-l] [-e BUCKETEXISTS] [-r REMOVEBUCKET]
                 [--listobjects LISTOBJECTS]
                 [--getbucketpolicy GETBUCKETPOLICY]
                 [--setbucketpolicy SETBUCKETPOLICY] [--bucket BUCKET]
                 [--getbucketnotification GETBUCKETNOTIFICATION]
                 [--getobject GETOBJECT]
                 shell

A command minio tools. Version:1.0.

positional arguments:
  shell                 connect the remote server as shell

optional arguments:
  -h, --help            show this help message and exit
  -m MAKEBUCKET, --makebucket MAKEBUCKET
                        create a new bucket.
  -l, --listbuckets     list the all buckets
  -e BUCKETEXISTS, --bucketexists BUCKETEXISTS
                        the bucket if exists
  -r REMOVEBUCKET, --removebucket REMOVEBUCKET
                        remove the buckets
  --listobjects LISTOBJECTS
                        list the all objects
  --getbucketpolicy GETBUCKETPOLICY
                        get bucket policy
  --setbucketpolicy SETBUCKETPOLICY
                        set bucket policy
  --bucket BUCKET, -b BUCKET
                        set bucket name
  --getbucketnotification GETBUCKETNOTIFICATION
                        get bucket notification
  --getobject GETOBJECT
                        get object from remote


```
