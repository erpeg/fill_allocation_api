import concurrent.futures
import utils
import multiprocessing as mp

number_of_servers = 3
fill_url = "http://localhost:8000/fill"

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for item in range(0,number_of_servers):
            executor.submit(utils.send_request(fill_url))
