from pathlib import Path
from storage.storage import JSONStorage, CSVStorage

class StorageFactory:

    @staticmethod
    def create(file_path):
        if not file_path:
            raise ValueError("Please select a valid File.")

        extension = Path(file_path).suffix.lower()

        if extension == ".json":
            return JSONStorage(file_path)
        elif extension == ".csv":
            return CSVStorage(file_path)
        else:
            raise ValueError("Unsupported File Format.")
