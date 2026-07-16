# How We Solve Optimal Account Balancing

Net each person's balance, then settle debts with minimum transfers via DFS matching.

## Steps

1. Aggregate net balance per person from all transactions.
2. Keep only non-zero balances.
3. DFS try pairing creditors and debtors to minimize transfer count.
