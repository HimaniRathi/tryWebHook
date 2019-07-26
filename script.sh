a = cat version.json | jq '.version'
echo $(($a + 1))