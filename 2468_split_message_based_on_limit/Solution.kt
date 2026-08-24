// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

class Solution {
    fun splitMessage(message: String, limit: Int): List<String> {
        val n = message.length
        for (parts in 1..n) {
            val sbDigits = parts.toString().length
            var ok = true
            var idx = 0
            val res = ArrayList<String>()
            for (i in 1..parts) {
                val tail = 3 + i.toString().length + sbDigits
                val cap = limit - tail
                if (cap <= 0 || idx >= n) {
                    ok = false
                    break
                }
                var take = cap
                if (take > n - idx) take = n - idx
                res.add(message.substring(idx, idx + take) + "<" + i + "/" + parts + ">")
                idx += take
            }
            if (ok && idx == n) return res
        }
        return emptyList()
    }
}
