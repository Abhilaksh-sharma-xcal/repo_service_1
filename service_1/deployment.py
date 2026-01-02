from ray import serve

@serve.deployment(
    name="hello_service"
)
class HelloService:
    def __init__(self):
        print("HelloService initialized")

    async def __call__(self, request):
        return {"message": "Hello from repo-hello-service"}
