# PyDBConnect
this is simply an API implementation (wrapper) for my WebAPI [PyDBConnect](https://github.com/nexus-novelist/PyDBConnect)

## How to use
Clone the PyDBConnect server repo on your server and follow the instructions
Use the Pypi package to use the API implementation

## Installation

```
pip install PyDBConnect
```

## Documentation

Import the library
```python
>>> from pydbconnect import connection
```

Establish a connection to the PyDBConnect server
```python
>>> db = connection("localhost:7575", "project", "password")
```
Replace the hostname with your own hostname/ip (making sure to include the port).
replace "project" with your PyDBConnect project name, and the password with your pyDBConnect password.

Check server availability
```python
>>> db.ping_db().status_code
```
ping_db() method returns a Response object which you can get the status code out of.
if the status code returned is 200 then the server responded properly!

Get list of collections in project
```python
>>> db.get_collections()
```
Should return a list of strings representing collections in the project

Get collection data
```python
>>> db.get_collection("collection")
```
Should return the documents present in the collection

Get document contents
```python
>>> db.get_document("collection", "document_id")
```
Returns the contents of the document

Create document
```python
>>> db.create_document("collection", "document_id", {"key": "value", "key2": "value3"})
```
Creates a new document with the specified document_id in the collection
(Oh no! i messed up the value2. Let's fix that!)

Update document
```python
>>> db.update_document("collection", "document_id", {"key": "value", "key2": "value2"})
```
Updates the document with the specified document_id in the collection

Delete document
```python
>>> db.delete_document("collection", "document_id")
```
Note: This returns a Response object

Create new collection
```python
>>> db.create_collection("new_collection")
```
Creates a new collection with the given name

Delete a collection
```python
>>> db.delete_collection("new_collection")
```
