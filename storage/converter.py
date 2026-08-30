from storage.storage_factory import StorageFactory
from tkinter import filedialog

class Converter:
    def convert(source_storage):

        destination = filedialog.asksaveasfilename(
            title = "Save File",
            defaultextension = ".csv",
            filetypes=[
                ("JSON Files", "*.json"),
                ("CSV Files", "*.csv")
            ]
        )

        destination_storage = StorageFactory.create(destination)

        expenses = source_storage.load_expenses()
        destination_storage.save_expenses(expenses)