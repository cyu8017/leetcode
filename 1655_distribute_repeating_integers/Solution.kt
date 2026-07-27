// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

class Solution {
    fun canDistribute(nums: IntArray, quantity: IntArray): Boolean {
        val freq = HashMap<Int, Int>()
        for (x in nums) freq[x] = (freq[x] ?: 0) + 1
        val cnt = freq.values.toList()
        quantity.sortDescending()
        val m = quantity.size
        val sums = IntArray(1 shl m)
        for (mask in 1 until (1 shl m)) {
            val bit = mask and -mask
            sums[mask] = sums[mask xor bit] + quantity[Integer.numberOfTrailingZeros(bit)]
        }
        var dp = hashSetOf(0)
        for (c in cnt) {
            val nxt = HashSet(dp)
            for (mask in dp) {
                val left = ((1 shl m) - 1) xor mask
                var sub = left
                while (sub > 0) {
                    if (sums[sub] <= c) nxt.add(mask or sub)
                    sub = (sub - 1) and left
                }
            }
            dp = nxt
        }
        return ((1 shl m) - 1) in dp
    }
}
