import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        with open(file, mode='rb') as f:
            a = f.read()
    except:
        raise FileNotFoundError(f'[Error 2] No such file or directory: {file}')
    else:
        return a
    finally:
        end_time = time.time()
        time_spent = end_time - start_time
        print(f'Time required for video2.mp4 = {time_spent}')

video_data = read_file_timed('file.txt')