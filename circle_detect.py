import os
import json

from collections import deque

DATA_DIR = 'nft_data/'


# for ERC 721
def detect_cycle(edges):
    graph = dict()  # account A to a list of next accounts, these are in the 'next' attribute as a list
    transact_time = dict() # {account address: time}, erase when backtrack
    cycle_occurence = dict() # the number of times in cycles
    visited = list()

    # sort edges in increasing order
    edges.sort(key=lambda transaction: transaction['time'])

    
    for edge in edges:
        if edge['from'] not in graph:
            graph[edge['from']] = deque()
        
        graph[edge['from']].append({
            'to': edge['to'],
            'time': edge['time'],
            'id': edge['id'] # transaction id
        })

    def dfs(address):
        if address in visited:
            return False

        visited.append(address)

        while address in graph and len(graph[address]) != 0:
            d = graph[address].popleft()
            if not dfs(d['to']):
                if address not in cycle_occurence:
                    cycle_occurence[address] = 0
                cycle_occurence[address] += 1

        return True

    # the start node is the node with smallest time
    start_address = edges[0]['from']
    dfs(start_address)

    return cycle_occurence

    

files = [file_name for file_name in os.listdir(DATA_DIR)]
files.sort()
for file_name in files:
    file_path = os.path.join(DATA_DIR, file_name)

    with open(file_path) as in_file:
        edges = []
        for line in in_file:
            d = eval(line)

            edges.append(d)
        
        print(edges[0]['asset']['tokenId'], detect_cycle(edges))
    
        
