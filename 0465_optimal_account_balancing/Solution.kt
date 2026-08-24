// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

class Solution {
    fun minTransfers(transactions: Array<IntArray>): Int {
        val balances = mutableMapOf<Int, Int>()
        for ((source, target, amount) in transactions) {
            balances[source] = balances.getOrDefault(source, 0) - amount
            balances[target] = balances.getOrDefault(target, 0) + amount
        }
        val debts = balances.values.filter { it != 0 }.toIntArray()
        return dfs(debts, 0)
    }

    private fun dfs(debts: IntArray, index: Int): Int {
        var currentIndex = index
        while (currentIndex < debts.size && debts[currentIndex] == 0) {
            currentIndex++
        }
        if (currentIndex == debts.size) {
            return 0
        }
        var best = debts.size
        for (nextIndex in currentIndex + 1 until debts.size) {
            if (debts[currentIndex].toLong() * debts[nextIndex] < 0) {
                debts[nextIndex] += debts[currentIndex]
                best = minOf(best, 1 + dfs(debts, currentIndex + 1))
                debts[nextIndex] -= debts[currentIndex]
            }
        }
        return best
    }
}
