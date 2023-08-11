from imy.BackEnd.backend import backend
from imy.FrontEnd.client import frontend
import asyncio
import sys

if __name__ == "__main__":
    if sys.argv[1] == "backend":
        asyncio.run(backend())

    if sys.argv[1] == "frontend":
        frontend()
