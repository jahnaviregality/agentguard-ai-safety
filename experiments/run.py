import json
from agentguard.core import load_scenarios, summarize

if __name__ == '__main__':
    for policy in ('every_action', 'sensitive_only'):
        print(json.dumps(summarize(load_scenarios(), policy), indent=2))
