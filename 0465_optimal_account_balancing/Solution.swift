// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

class Solution {
    func minTransfers(_ transactions: [[Int]]) -> Int {
        var balances: [Int: Int] = [:]
        for transaction in transactions {
            let source = transaction[0]
            let target = transaction[1]
            let amount = transaction[2]
            balances[source, default: 0] -= amount
            balances[target, default: 0] += amount
        }

        var debts = balances.values.filter { $0 != 0 }
        return dfs(debts: &debts, index: 0)
    }

    private func dfs(debts: inout [Int], index: Int) -> Int {
        var current = index
        while current < debts.count && debts[current] == 0 {
            current += 1
        }
        if current == debts.count {
            return 0
        }

        var best = debts.count
        for nextIndex in (current + 1)..<debts.count {
            if debts[current] * debts[nextIndex] < 0 {
                debts[nextIndex] += debts[current]
                best = min(best, 1 + dfs(debts: &debts, index: current + 1))
                debts[nextIndex] -= debts[current]
            }
        }
        return best
    }
}
