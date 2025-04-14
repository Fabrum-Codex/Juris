from juris.knowledge import load_knowledge
from juris.logging import get_logger
from juris.query import query

logger = get_logger(__name__)

result = query("Someone commited 2 murders by accident, what is a judgement for this ?")
logger.debug(result)