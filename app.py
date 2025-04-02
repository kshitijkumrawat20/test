from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Configure CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Set the complete N8N webhook URL
EC2_HTTP_URL = "http://ec2-13-58-27-158.us-east-2.compute.amazonaws.com:5678/webhook/0b95a964-2518-4250-929c-0e6f6ba766ab"

@app.post("/")
async def proxy_request(request: Request):
    try:
        body = await request.json()  # Get JSON body from request
        async with httpx.AsyncClient() as client:
            response = await client.post(EC2_HTTP_URL, json=body)  # Forward request to N8N webhook
        return response.json()  # Return response from N8N
    except Exception as e:
        return {"error": str(e)}
