// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/


class Solution {
    fun shoppingOffers(price: List<Int>, special: List<List<Int>>, needs: List<Int>): Int {
        val memo = HashMap<List<Int>, Int>()
        fun dfs(cur: List<Int>): Int {
            memo[cur]?.let { return it }
            var best = 0
            for (i in cur.indices) best += cur[i] * price[i]
            for (offer in special) {
                val next = ArrayList<Int>()
                var ok = true
                for (i in cur.indices) {
                    val remain = cur[i] - offer[i]
                    if (remain < 0) { ok = false; break }
                    next.add(remain)
                }
                if (ok) best = minOf(best, offer.last() + dfs(next))
            }
            memo[cur] = best
            return best
        }
        return dfs(needs)
    }
}
