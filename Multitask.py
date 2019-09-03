from multiprocessing import Process, Pipe

class MProcessPipe:

    @staticmethod
    def spawn(process_function):
        main_pipe, process_pipe = Pipe()
        process = Process(target=process_function, args=(process_pipe,))
        process.start()
        process.join()
        return process, main_pipe