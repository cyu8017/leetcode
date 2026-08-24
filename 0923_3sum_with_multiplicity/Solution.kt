// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

class Solution {
    fun threeSumMulti(arr: IntArray, target: Int): Int {
        val MOD = 1_000_000_007
        val count = LongArray(101)
        for (x in arr) count[x]++
        var ans = 0L
        for (a in 0..100) if (count[a] > 0) {
            for (b in a..100) if (count[b] > 0) {
                val c = target - a - b
                if (c < b || c > 100 || count[c] == 0L) continue
                ans += when {
                    a == b && b == c -> count[a] * (count[a] - 1) * (count[a] - 2) / 6
                    a == b -> count[a] * (count[a] - 1) / 2 * count[c]
                    b == c -> count[a] * count[b] * (count[b] - 1) / 2
                    else -> count[a] * count[b] * count[c]
                }
            }
        }
        return (ans % MOD).toInt()
    }
}
