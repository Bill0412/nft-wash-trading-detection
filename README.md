# Wash Trading Cycle Detection

This project applies DFS to ERC721 NFT trading time-series transactions to find out the probability of a trader performing wash trading.

## Algorithm Time Complexity
The time complexity for this project is **O(E)**, while in reference 1, the algorithm to detect cycles is claimed to be **O((N+E)(C+1))**.

- **E**: the number of edges in the graph, i.e., the number of transfer and trade.
- **N**: the number of nodes in the graph, i.e., the number of users that bought the NFT.
- **C**: the number of cycles in the graph.

Note: the sample data does not include the transfer data. So it only counts counts cycles before first transfer of an NFT.

## References
Thie project is based on the following paper and improves it in terms of algorithmic time complexity.

1. NFT Wash Trading - Quantifying suspicious behaviour in NFT markets: https://arxiv.org/pdf/2202.03866.pdf