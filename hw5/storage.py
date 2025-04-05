from datetime import datetime
from abc import ABC, abstractmethod

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, file_data: bytes, file_path: str) -> None:
        """
                Сохранить файл (данные файла) по указанному пути
                или в конкретном месте (в облаке, локально и т.п.).
        """

        pass

    @abstractmethod
    def load(self, file_path: str) -> bytes:
        """
                Загрузить файл (данные файла) по указанному пути
                (локально, из облака и т.п.).
        """

        pass

    @abstractmethod
    def __delete__(self, file_path: str) -> None:
        """
                Удалить файл.
        """

        pass


class CloudStorage(StorageStrategy):
    def save(self, file_data: bytes, file_path: str) -> None:
        print(f"Сохраняем файл из облака: {file_path}")

    def load(self, file_path: str) -> bytes:
        print(f"Загружаем файл из облака: {file_path}")

    def delete(self, file_path: str) -> None:
        print(f"Удаляем файл из облака: {file_path}")


class LocalStorage(StorageStrategy):
    def save(self, file_data: bytes, file_path: str) -> None:
        print(f"Сохраняем файл локально: {file_path}")

    def load(self, file_path: str) -> bytes:
        print(f"Загружаем файл с локального диска: {file_path}")

        return b"file data"

    def delete(self, file_path: str) -> None:
        print(f"Удаляем файл с локального диска: {file_path}")
