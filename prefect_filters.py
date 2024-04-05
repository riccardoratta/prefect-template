import logging
import re

_filter_patterns = [
    r"Created task run '.+' for task '.+'",
    r"Executing '.+' immediately...",
    r"Finished in state Completed\(\)",
    r"Downloading flow code from storage at '.+'",
    r"Opening process...",
    r"Created subflow run '.+' for flow '.+'",
]


# This class is used to remove redundant messages by Prefect
class RemoveCreatedTaskRun(logging.Filter):
    def filter(self, record):
        for pattern in _filter_patterns:
            match = re.search(pattern, record.msg)
            if match:
                return False

        return True
