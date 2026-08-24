// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/


class Solution {
    fun maxNumberOfAlloys(
        n: Int,
        k: Int,
        budget: Int,
        composition: List<List<Int>>,
        stock: List<Int>,
        cost: List<Int>,
    ): Int {
        var lo = 0L
        var hi = 1_000_000_000L
        var ans = 0L
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            if (ok(mid, n, budget, composition, stock, cost)) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans.toInt()
    }

    private fun ok(
        machines: Long,
        n: Int,
        budget: Int,
        composition: List<List<Int>>,
        stock: List<Int>,
        cost: List<Int>,
    ): Boolean {
        for (comp in composition) {
            var spend = 0L
            for (i in 0 until n) {
                val need = machines * comp[i] - stock[i]
                if (need > 0) spend += need * cost[i]
            }
            if (spend <= budget) return true
        }
        return false
    }
}
