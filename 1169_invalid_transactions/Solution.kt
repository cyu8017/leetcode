// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

class Solution {
    fun invalidTransactions(transactions: Array<String>): List<String> {
        val n = transactions.size
        val name = Array(n) { "" }
        val time = IntArray(n)
        val amount = IntArray(n)
        val city = Array(n) { "" }
        for (i in 0 until n) {
            val p = transactions[i].split(",")
            name[i] = p[0]
            time[i] = p[1].toInt()
            amount[i] = p[2].toInt()
            city[i] = p[3]
        }
        val invalid = linkedSetOf<String>()
        for (i in 0 until n) {
            if (amount[i] > 1000) invalid.add(transactions[i])
            for (j in 0 until n) {
                if (i != j && name[i] == name[j] && city[i] != city[j] && kotlin.math.abs(time[i] - time[j]) <= 60) {
                    invalid.add(transactions[i])
                    invalid.add(transactions[j])
                }
            }
        }
        return invalid.toList()
    }
}
