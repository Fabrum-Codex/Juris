from juris.knowledge import load_knowledge
from juris.logging import get_logger
from juris.query import query

logger = get_logger(__name__)

import argparse

def get_args():
	parser = argparse.ArgumentParser(description="Choose either --query or --load")

	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--query', nargs=1, metavar='queryString', help='Run a query')
	group.add_argument('--load', action='store_true', help='Load from previous run')

	args = parser.parse_args()

	query_string = args.query[0] if args.query else None
	return args, query_string

if __name__ == "__main__":
	args, query_string = get_args()

	if args.query:
		result = query(query_string)
		logger.debug(result["result"])
	elif args.load:
		logger.debug("Load mode activated")


