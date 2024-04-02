import time


def measure_execution_time(get_reposnse):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        result = get_reposnse(request, *args, **kwargs)
        end_time = time.time()

        print(f"{request.method} / Executed in {end_time - start_time} seconds")

        return result

    return middleware
