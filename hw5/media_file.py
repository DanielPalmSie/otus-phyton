from abc import ABC, abstractmethod
from datetime import datetime
from hw5.storage import StorageStrategy

class MediaFile(ABC):
    def __init__(
        self,
        name: str,
        size: int,
        creation_date: datetime,
        owner: str,
        storage_strategy: StorageStrategy,
    ):
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.owner = owner
        self.storage_strategy = storage_strategy

        @abstractmethod
        def convert(self, target_format: str) -> None:
            """
            Преобразовать файл в другой формат (аудио, видео и т.д.).
            Метод будет по-разному реализовываться в наследниках.
            """
            pass

        @abstractmethod
        def extract_features(self) -> dict:
            """
            Извлечь некоторые фичи/метаданные из файла:
            например, для аудио — битрейт, длительность;
            для фото — разрешение, EXIF-данные и т.д.
            """
            pass

        def save(self, file_data: bytes) -> None:
            """
            Сохранить файл, используя выбранную стратегию хранения.
            """
            print(f"Сохраняем файл '{self.name}'...")
            self.storage_strategy.save(file_data, self.name)

        def load(self) -> bytes:
            """
            Загрузить файл (данные) с помощью стратегии хранения.
            """
            print(f"Загружаем файл '{self.name}'...")
            return self.storage_strategy.load(self.name)

        def delete(self) -> None:
            """
            Удалить файл.
            """
            print(f"Удаляем файл '{self.name}'...")
            self.storage_strategy.delete(self.name)


class AudioFile(MediaFile):
    def __init__(
        self,
        name: str,
        size: int,
        creation_date: datetime,
        owner: str,
        storage_strategy: StorageStrategy,
        bitrate: int,
        duration_sec: float
    ):
        super().__init__(name, size, creation_date, owner, storage_strategy)
        self.bitrate = bitrate
        self.duration_sec = duration_sec

    def convert(self, target_format: str) -> None:
        print(f"Конвертируем аудио '{self.name}' в формат {target_format}...")


    def extract_features(self) -> dict:
        print(f"Извлекаем метаданные аудио '{self.name}'...")

        return {
            "bitrate": self.bitrate,
            "duration_sec": self.duration_sec,
        }

class VideoFile(MediaFile):
    def __init__(
        self,
        name: str,
        size: int,
        creation_date: datetime,
        owner: str,
        storage_strategy: StorageStrategy,
        resolution: str,
        fps: int,
        duration_sec: float,
    ):
        super().__init__(name, size, creation_date, owner, storage_strategy)
        self.resolution = resolution
        self.fps = fps
        self.duration_sec = duration_sec

    def convert(self, target_format: str) -> None:
        print(f"Конвертируем видео '{self.name}' в формат {target_format}...")

    def extract_features(self) -> dict:
        print(f"Извлекаем метаданные видео '{self.name}'...")
        return {
            "resolution": self.resolution,
            "fps": self.fps,
            "duration_sec": self.duration_sec,
        }

class PhotoFile(MediaFile):
    def __init__(
        self,
        name: str,
        size: int,
        creation_date: datetime,
        owner: str,
        storage_strategy: StorageStrategy,
        resolution: str,
        camera_model: str,
    ):
        super().__init__(name, size, creation_date, owner, storage_strategy)
        self.resolution = resolution
        self.camera_model = camera_model

    def convert(self, target_format: str) -> None:
        print(f"Конвертируем фото '{self.name}' в формат {target_format}...")

    def extract_features(self) -> dict:
        print(f"Извлекаем метаданные фото '{self.name}'...")
        return {
            "resolution": self.resolution,
            "camera_model": self.camera_model,
        }