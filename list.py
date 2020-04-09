import boto.ec2
import boto.s3

conn=boto.ec2.connect_to_region("us-east-1")
reservations = conn.get_all_instances()
for res in reservations:
    for inst in res.instances:
        if 'Name' in inst.tags:
            print "%s (%s) [%s]" % (inst.tags['Name'], inst.id, inst.state)
        else:
            print "%s [%s]" % (inst.id, inst.state)
			
conn=boto.s3.connect_to_region("us-east-1")
reservations2 = conn.get_all_instances()
for res in reservations2:
    for inst in res.instances:
        if 'Name' in inst.tags:
            print "%s (%s) [%s]" % (inst.tags['Name'], inst.id, inst.state)
        else:
            print "%s [%s]" % (inst.id, inst.state)	  		 
			
			
			