from enum import Enum

class PrintStatus(Enum):
    SUCCESS = 0
    FAILURE = 1
    IN_PROGRESS = 2
    NOT_STARTED = 3
    

    def __str__(self) -> str:
        if self == PrintStatus.SUCCESS:
            return "Completed"
        if self == PrintStatus.FAILURE:
            return "Failed"
        if self == PrintStatus.IN_PROGRESS:
            return "Printing"
        if self == PrintStatus.NOT_STARTED:
            return "Not started"
        
        return ""
    

def str_to_printstatus(input: str) -> PrintStatus:
    if input.lower() == "completed":
        return PrintStatus.SUCCESS
    if input.lower() == "failed":
        return PrintStatus.FAILURE
    if input.lower() == "printing":
        return PrintStatus.IN_PROGRESS
    if input.lower() == "not started":
        return PrintStatus.NOT_STARTED