import zipfile
import os
import ftplib                                          
import sys
import paramiko 

def make_zip(zip_file_name):
    try:
        os.remove(zip_file_name)
    except:
        pass
    target_dir = '.'
    zip = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        if base == 'paramiko' or '.git' in base:
            pass
        else:
            for f in files:
                fn = os.path.join(base, f)
                zip.write(fn, fn[rootlen:])
            
def scp_transfer(zip_name,hostname,aws_username,password,assignment_name):

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, username=aws_username, key_filename=None, password=password)
    sftp = ssh_client.open_sftp()
    sftp.put(zip_name, "%s/%s" % (assignment_name,zip_name))#'~/' + assignment_name + '/' + filename)
    sftp.close()
    ssh_client.close()

users = ['godwin.adjaho',
         'osborn.kwarteng.adu',
         'samuel.ako',
         'clement.yao.amedume',
         'emmanuel.anim',
         'linda.ansong',
         'adelaide.atakora',
         'claude.ayitey',
         'akua.baning',
         'dominic.fui.dodzi-nusenu',
         'samuel.dzidzornu',
         'eric.engmann',
         'albert.fiati-kumasenu',
         'joel.funu',
         'francis.kofigah',
         'angela.koranteng',
         'samuel.kyemenu-sarsah',
         'hadi.mukaila',
         'nicodemus.nutsukpui',
         'christian.osei-bonsu',
         'precious.ewusi.nyarko',
         'elisha.senoo',
         'tenace.setor',
         'gbeila.aliu.wahab',
         'yaw.boakye.yiadom']

def main(users):
    username = raw_input('What is your mest user_name (same as e-mail)\n')
    if username not in users:
        print 'Please enter a name from the following %s' % str(names)
        sys.exit(1)
    hostname = 'ec2-107-20-64-184.compute-1.amazonaws.com'
    aws_username = 'tech2014'
    password = 'azontofiesta'
    zip_name = '%s.zip' % username
    #NOTE: THE FOLLOWING SHOULD BE CHANGED WITH EACH ASSIGNMENT
    assignment_name = 'currencyAssignment'
    make_zip(zip_name)
    scp_transfer(zip_name=zip_name,hostname=hostname,aws_username=aws_username,
                 password=password,assignment_name=assignment_name)

if __name__ == '__main__':
    #Currently, users is hardcoded.  To be changed in the future.
    #Perhaps takes a command line argument
    if users:
        main(users)
    else:
        pass
