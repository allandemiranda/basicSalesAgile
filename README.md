# basicSalesAgile
BASIC SALES APP AGILE SOLUTIONS

cd api/

openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 -subj "/"

cd ../web

rm -R node_modules/

rm package-lock.json

cd ..

docker-compose up -d
