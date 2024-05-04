import requests
from requests import Response


class connection:
    def __init__(self, hostname, project, password):
        self.hostname = hostname
        self.project = project
        self.password = password

    def ping_db(self) -> Response:
        """
        Pings the database server to check if there is a proper connection available
        Returns: Response
        """
        return requests.get(self.hostname)

    def get_collections(self) -> list[str]:
        """
        Returns a list of collections for the given project (list[str])
        """
        return requests.get(
            self.hostname + "/get/" + self.project + "/" + self.password
        ).content

    def get_collection(self, collection) -> dict:
        """
        Returns the data of the given collection (dict)
        """
        return requests.get(
            self.hostname
            + "/get/"
            + self.project
            + "/"
            + collection
            + "/"
            + self.password
        ).content

    def get_document(self, collection, document) -> dict:
        """
        Returns the data of the given document (dict)
        """
        return requests.get(
            self.hostname
            + "/get/"
            + self.project
            + "/"
            + collection
            + "/"
            + document
            + "/"
            + self.password
        ).content

    def create_document(self, collection, document_id, content) -> dict:
        """
        Creates a new document in the given collection

        Returns: contents of the new document (dict)
        """
        return requests.post(
            self.hostname
            + "/create-document/"
            + self.project
            + "/"
            + collection
            + "/"
            + document_id
            + "/"
            + self.password,
            content,
        ).content

    def update_document(self, collection, document_id, content) -> dict:
        """
        Updates an existing document in the given collection

        Returns: contents of the updated document (dict)
        """
        return requests.put(
            self.hostname
            + "/update-document/"
            + self.project
            + "/"
            + collection
            + "/"
            + document_id
            + "/"
            + self.password,
            content,
        ).content

    def delete_document(self, collection, document_id) -> Response:
        """
        Deletes document from the collection

        Returns: Response
        """
        return requests.delete(
            self.hostname
            + "/delete-document/"
            + self.project
            + "/"
            + collection
            + "/"
            + document_id
            + "/"
            + self.password
        )

    def create_collection(self, collection) -> Response:
        """
        Creates a new collection in the given project.

        Returns: Response
        """
        return requests.post(
            self.hostname
            + "/create-collection/"
            + self.project
            + "/"
            + collection
            + "/"
            + self.password
        )

    def delete_collection(self, collection) -> Response:
        """
        Deletes the given collection from the project.

        Returns: Response
        """

        return requests.delete(
            self.hostname
            + "/delete-collection/"
            + self.project
            + "/"
            + collection
            + "/"
            + self.password
        )
