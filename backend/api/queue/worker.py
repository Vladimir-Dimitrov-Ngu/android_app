from rq import Worker, Queue, Connection
from redis import Redis

redis_conn = Redis(host='localhost', port=6379, db=0)
queue = Queue(connection=redis_conn)
worker = Worker([queue], connection=redis_conn)
if __name__ == '__main__':
    print("Worker is starting...")
    worker.work()
    print("Worker has finished.")
