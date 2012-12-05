EIT="godwin.adjaho"
rm -fr $EIT
mkdir $EIT
unzip -d $EIT $EIT.zip
cp check.py $EIT/check.py
cd $EIT
python check.py $EIT > ../grade.csv
cd ..
echo $EIT
appcfg.py upload_data --config_file=gradeloader.py --filename=grade.csv --kind=Grade --url=http://localhost:8080/_ah/remote_api