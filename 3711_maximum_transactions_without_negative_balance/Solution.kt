// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

class Solution {
    fun maxTransactions(transactions: IntArray): Int {
        var tm = TreeMap<Int, Int>()
        var ans = transactions.size
        var s = 0
        for (x in transactions) {
            s += x
            tm.merge(x, 1, { a, b -> a + b })
            while (s < 0) {
                var y = tm.firstKey()
                s -= y
                ans--
                var c = tm[y]
                if (c == 1) tm.remove(y)
                else tm[y] = c - 1
            }
        }
        return ans
    }
}
