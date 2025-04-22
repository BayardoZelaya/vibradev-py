import httpx
class ApplicationCalls:
    def __init__(self):
        print("ApplicationCalls module instantiated.")
    
    async def call_go_service(self, service_name):
        """
        Makes an HTTP GET request to the Go service and returns the response text.
        """
        self.service_name = service_name

        async with httpx.AsyncClient() as client:
            response = await client.get(self.service_name)
            return response.text