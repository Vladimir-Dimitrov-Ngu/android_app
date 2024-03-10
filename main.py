from concurrent.futures import ThreadPoolExecutor

import uvicorn

from backend.api.queue import worker
from backend.app import app_fastapi
from frontend.app_main_menu import app_dash as app_dash_menu
from frontend.app_register import app_dash as app_dash_register


def run_menu():
    app_dash_menu.run_server(debug=False, port=9001)


def run_register():
    app_dash_register.run_server(debug=False, port=9000)


def run_fastapi():
    uvicorn.run(app_fastapi, host="0.0.0.0", port=9002, reload=False)


def run_worker():
    print("Worker is starting...")
    worker.work()


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_worker = executor.submit(worker)
        future_fastapi = executor.submit(run_fastapi)
        future_menu = executor.submit(run_menu)
        future_register = executor.submit(run_register)
        executor.shutdown(wait=True)
        # ThreadPoolExecutor.wait([future_fastapi, future_menu, future_register, worker])
