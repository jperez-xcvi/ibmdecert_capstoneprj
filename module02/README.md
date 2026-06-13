## 1. Download catalog.json:
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json
```

## 2. Copy file `catalog.json` to mongo container
```bash
docker cp catalog.json mongodb_container:/tmp/catalog.json
```
## 3. Import data to Mongo

**input**
```bash
docker exec -it mongodb_container mongoimport --username root --password HL3yqZKrqlX4RM --authenticationDatabase admin --db catalog --collection electronics --file /tmp/catalog.json
```
**output**
```
2026-06-13T01:17:04.387+0000    connected to: mongodb://localhost/
2026-06-13T01:17:04.420+0000    438 document(s) imported successfully. 0 document(s) failed to import.
```
## 4. Enter to Mongo Container

**input**
```bash
docker exec -it mongodb_container mongosh -u root -p HL3yqZKrqlX4RM --authenticationDatabase admin
```
**output**
Wished Behaviour: Now we are in Mongo Shell!! (see `test>` in the CLI)

## 5. List databases in the Mongo Server

**input**
```mongosh
show dbs
```
**output**
```
admin    100.00 KiB
catalog   48.00 KiB
config    12.00 KiB
local     72.00 KiB
```
## 6. Switch to "catalog" database" and show its collections

**input**
```javascript
use catalog
```
**output**
Wished Behaviour: Now we are in catalog database!! (see `catalog>` in the CLI)

**input**
```javascript
show collections
```
**output**
```
electronics
```
## 7. Create index in the field "type"

**input**
```javascript
db.electronics.createIndex({ type: 1 })
```
**output**
```
type_1
```

## 8. Count "laptops"

**input**
```javascript
db.electronics.countDocuments({ type: "laptop" })
```
**output**
```
389
```

## 9. Count 6 inches smartphones

**input**
```javascript
db.electronics.countDocuments({ type: "smart phone", "screen size": 6 })
```

**output**
```
8
```
## 10. Average screen size

**input**
```javascript
db.electronics.aggregate([
  { $match: { type: "smart phone" } },
  { $group: { _id: "$type", average_screen_size: { $avg: "$screen size" } } }
])
```
**output**
```
[ { _id: 'smart phone', average_screen_size: 6 } ]
```
Above query was the last one so we need to type `exit` in mongo shell to return main CLI

## 11. Export to csv

**input**
```bash
docker exec -it mongodb_container mongoexport --username root --password HL3yqZKrqlX4RM --authenticationDatabase admin --db catalog --collection electronics --type=csv --fields _id,type,model --out /tmp/electronics.csv
```
**output**
```
2026-06-13T01:55:28.994+0000    connected to: mongodb://localhost/
2026-06-13T01:55:29.026+0000    exported 438 records
```
In this moment the required csv file is in Docker container with mongo `mongodb_container`  so we need copy this file to required path of out main host by this way:
**input**
```bash
docker cp mongodb_container:/tmp/electronics.csv ./module02/electronics.csv
```

**output**
```
Successfully copied 20.3kB (transferred 22kB) to /home/jose/projects/ibmdecert_capstoneprj/module02/electronics.csv
```


