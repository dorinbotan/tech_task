FROM mongo

COPY data.json /home/data.json
CMD mongoimport --host mongodb --db orbital_witness --collection titles --type json --file /home/data.json --jsonArray
