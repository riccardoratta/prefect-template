import asyncio

from example.utils.prefect import get_deployment_name, get_logger
from prefect import flow, task


@task()
def a_task(another_parameter: str):
    l = get_logger()
    l.info(f"Converting the string {another_parameter} to uppercase.")
    return another_parameter.upper()


@flow()
def my_flow(some_parameter: int):
    l = get_logger()
    l.info("Starting my flow..")
    for i in range(some_parameter):
        a_task(f"example-{i}")


if __name__ == "__main__":
    asyncio.run(my_flow.serve(f"my-flow:{get_deployment_name()}"))
