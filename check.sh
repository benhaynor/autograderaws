EIT=$1
ASSIGNMENT=$2
OUTDIR="./$ASSIGNMENT/$EIT"
EMAIL="ben@meltwater.org"
PASSWORD="2msterDAM"
DOMAIN="localhost:8080"
echo $OUTDIR
rm -fr $OUTDIR
mkdir $OUTDIR
unzip -d $OUTDIR $EIT'.zip'
cd $ASSIGNMENT
cp check.py $EIT'/check.py'
cd $EIT
python check.py $EIT > '../../grade.csv'
cd ../..
URL="http://$DOMAIN/_ah/remote_api"
echo $URL
echo $PASSWORD | appcfg.py upload_data --email=$EMAIL --config_file=loader.py --filename=grade.csv --kind=Grade --url=$URL --passin
rm bulkloader*
#rm EIT*