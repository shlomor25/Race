import pymongo
client = pymongo.MongoClient("mongodb+srv://admin:<password>@race-hynwe.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

#
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# #print(client.changestream.collection.insert_one({"hello": "world"}).inserted_id)
# db = client["race"]
# mycol = mydb["files"]
#
# mydict = { "name": "John", "address": "Highway 37" }
#
# x = mycol.insert_one(mydict)
# mydict = { "name": "Peter", "address": "Lowstreet 27" }
#
# x = mycol.insert_one(mydict)
#
# print(x.inserted_id)

try:
    resume_token = None
    pipeline = [{'$match': {'operationType': 'insert'}}]
    with db.collection.watch(pipeline) as stream:
        for insert_change in stream:
            print(insert_change)
            resume_token = stream.resume_token
except pymongo.errors.PyMongoError as e:
    # The ChangeStream encountered an unrecoverable error or the
    # resume attempt failed to recreate the cursor.
    if resume_token is None:
        print(e)
        # There is no usable resume token because there was a
        # failure during ChangeStream initialization.
        #logging.error('...')
    else:
        # Use the interrupted ChangeStream's resume token to create
        # a new ChangeStream. The new stream will continue from the
        # last seen insert change without missing any events.
        with db.collection.watch(
                pipeline, resume_after=resume_token) as stream:
            for insert_change in stream:
                print(insert_change)