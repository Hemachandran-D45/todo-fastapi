def decode(doc) -> dict:
    return {
        "_id":doc._id,
        "title":doc.todo,
        'timestamp':doc.timestamp
    }


def decode_todos(docs) -> list:
    return[
        decode(doc) for doc in docs
    ]