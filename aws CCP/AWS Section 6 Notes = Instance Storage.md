## EBS overview
- an **EBS VOLUME** is a network drive (storage) you can attach to your instances while they run ,which means there might be a bit of latency 
- it allows your instances to conserve data , even after the termination of instance like hard drives
- the whole purpose is to have the ability to recreate an instance and mount the same EBS volume from before and get back data
*Note : at the CCP level , only one EBS get mounted to one EC2 isntance* but many EBS get mounted to one EC2 instance 
 - when you create an EBS volume , it is bound to a specific AZ 
 - analogy : think of them as a "Network USB stick" that u can  take from a computer to another
 - to move a volume across different AZs , you need to snapshot it
 - you get billed for all the predefined capacity 
 - delete on termination is an option that should be defined at the creation of the root EBS volume
## EBS Snapshots 
- a snapshot works as a backup for your EBS volume at any point in time u created , even after terminating the Volume / not necessary to detach volume to do snapshot but its recommended 
- why we do snapshots : 
	1. Can copy and restore snapshots across AZ or region 
	- EBS Snapshots Features : 
	  1. EBS Snapshot Archive : allows you to move a snapshot to an "ARCHIVE TIER" that is 75% cheaper / it takes between 24 to 72 hours to restore it from the archive (least imoortant to you)
	  2. Recycle Bin for EBS Snapshots : setup rules to retain deleted snapshots so you can recover them after an accidental deletion / specify retention to protect your snapshots

## AMI Overview 
