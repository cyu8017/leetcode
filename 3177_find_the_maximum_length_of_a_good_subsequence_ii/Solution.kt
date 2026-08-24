// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

class Solution {
    fun maximumLength(nums: IntArray, k: Int): Int {
        val n = nums.size
        val f = Array(n) { IntArray(k + 1) }
        val mp = Array(k + 1) { HashMap<Int, Int>() }
        val g = Array(k + 1) { IntArray(3) }
        var ans = 0
        for (i in 0 until n) {
            for (h in 0..k) {
                f[i][h] = mp[h].getOrDefault(nums[i], 0)
                if (h > 0) {
                    if (g[h - 1][0] != nums[i]) {
                        f[i][h] = maxOf(f[i][h], g[h - 1][1])
                    } else {
                        f[i][h] = maxOf(f[i][h], g[h - 1][2])
                    }
                }
                f[i][h]++
                mp[h][nums[i]] = maxOf(mp[h].getOrDefault(nums[i], 0), f[i][h])
                if (g[h][0] != nums[i]) {
                    if (f[i][h] >= g[h][1]) {
                        g[h][2] = g[h][1]
                        g[h][1] = f[i][h]
                        g[h][0] = nums[i]
                    } else if (f[i][h] > g[h][2]) {
                        g[h][2] = f[i][h]
                    }
                } else if (f[i][h] > g[h][1]) {
                    g[h][1] = f[i][h]
                }
                ans = maxOf(ans, f[i][h])
            }
        }
        return ans
    }
}
