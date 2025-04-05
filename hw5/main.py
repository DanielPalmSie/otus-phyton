from hw5.media_file import AudioFile
from hw5.storage import LocalStorage

if __name__ == "__main__":

    local_storage = LocalStorage()

    # Создаём аудиофайл
    audio = AudioFile(
        name="song.mp3",
        size=4000,
        creation_date=datetime.now(),
        owner="Alice",
        storage_strategy=local_storage,
        bitrate=320,
        duration_sec=180.0
    )

    # Сохраняем аудио (фейковые данные)
    audio.save(b"audio file data")

    # Загружаем аудио
    audio_data = audio.load()

    # Извлекаем фичи (метаданные)
    features = audio.extract_features()
    print("Извлечённые метаданные аудио:", features)

    # Конвертируем аудио
    audio.convert(target_format="wav")

    # Удаляем аудио
    audio.delete()