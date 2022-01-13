kaggle kernels pull kiitand/another-sleep -m
kaggle kernels push 
echo "sleeping for 600 seconds"
sleep 600


echo "I'm awake!"
RESPONSE=$(kaggle kernels status kiitand/another-sleep)
while [[ ! $RESPONSE == *"complete"* ]]
do
echo "not done yet, sleeping for 200 seconds"
sleep 200
RESPONSE=$(kaggle kernels status kiitand/another-sleep)
done
echo "done"
#download outputs
find ../DownloadTest -delete
kaggle kernels output -p ../DownloadTest kiitand/another-sleep
echo 'done'

shopt -s extglob
mkdir ../PullTemp                                           # create temp folder
V1=`find ../DownloadTest -type d -name "sleep"`             # get the first set of picture outputs
mv $V1 ../PullTemp/sleep                                    # move to temp folder
V2=`find ../DownloadTest/swin -type d -name "SwinIR_large"` # get the second set of picture outputs
mv $V2 ../PullTemp/swin                                     # move to temp folder
mv ../DownloadTest/info.txt ../PullTemp                     # move info file to temp folder
rm -r ../DownloadTest/*                                     # delete unneeded files
cp -r ../PullTemp/* ../DownloadTest                         # move files back from temp folder
rm -r ../PullTemp                                           # delete temp folder
python create_vid.py
python sendtweets.py

