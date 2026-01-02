from ray import serve

@serve.deployment(
    name="hello_service_0"
)
class HelloService0:
    def __init__(self):
        print("HelloService initialized")

    async def __call__(self, request):
        return {"message": "Hello from repo-hello-service"}


@serve.deployment(
    name="hello_service_1"
)
class HelloService1:
    def __init__(self):
        print("HelloService initialized")

    async def __call__(self, request):
        return {"message": "Hello from repo-hello-service"}


@serve.deployment(
    name="hello_service_2"
)
class HelloService2:
    def __init__(self):
        print("HelloService initialized")

    async def __call__(self, request):
        return {"message": "Hello from repo-hello-service"}