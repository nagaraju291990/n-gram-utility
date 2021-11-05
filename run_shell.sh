input=$1
output=$2


#echo $input

mkdir $output -p

for file in $input/*
do
  f=$(basename "$file")
  echo "Running $f"
  python3 n_gram_generator.py -i=$file -n=1 > "$2/$f"1.out
  python3 n_gram_generator.py -i=$file -n=2 > "$2/$f"2.out
  python3 n_gram_generator.py -i=$file -n=3 > "$2/$f"3.out
  python3 n_gram_generator.py -i=$file -n=4 > "$2/$f"4.out
done
