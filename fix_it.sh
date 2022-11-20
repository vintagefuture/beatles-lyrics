for file in $(ls ALL/*.txt)
do
echo -e "$(cat "$file")\n" >> total.txt
done
