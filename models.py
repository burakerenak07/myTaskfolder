from fastapi import FastAPI,Path,Query,HTTPException,status
from typing import Optional
from pydantic import BaseModel
from uuid import UUID,uuid4
from typing import Optional,List
from enum import Enum

class webLink(BaseModel):
    id: UUID = None
    myLink : str