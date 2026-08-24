// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

class Solution {
    fun maxItems(items: Array<IntArray>, budget: Int): Int {
        val n = items.size
        val frequency = IntArray(n + 1)
        var minimumPrice = items[0][1]
        for (item in items) {
            frequency[item[0]]++
            minimumPrice = minOf(minimumPrice, item[1])
        }
        val batches = ArrayList<IntArray>()
        for (item in items) {
            var gain = 0
            var multiple = item[0]
            while (multiple <= n) {
                gain += frequency[multiple]
                multiple += item[0]
            }
            gain--
            if (gain > 0 && item[1] < 2 * minimumPrice) batches.add(intArrayOf(item[1], gain))
        }
        batches.sortBy { it[0] }
        var remaining = budget.toLong()
        var answer = (budget / minimumPrice).toLong()
        var boosted = 0L
        for (current in batches) {
            var count = current[1].toLong()
            val affordable = remaining / current[0]
            if (affordable < count) count = affordable
            remaining -= count * current[0]
            boosted += count
            val total = 2 * boosted + remaining / minimumPrice
            if (total > answer) answer = total
            if (count < current[1]) break
        }
        return answer.toInt()
    }
}
