echo "
Destroying current build images
"
docker-compose down
sleep 5

echo "
  creating docker image
"
sleep 2
docker-compose up --build -d

sleep 5
echo "
  build process complete you can check server by login to server http://127.0.0.1:8050/admin/
  using username: user and password: user
"
echo 10
echo "
  testing docker image
"
docker-compose -f docker-compose-test.yml run tests