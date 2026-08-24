// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

class Solution {
    fun minSteps(left: Int, right: Int, start: Int): Int {
        if (right <= start) return start - left
        if (left >= start) return right - start
        return minOf((start - left) + (right - left), (right - start) + (right - left))
    }

    fun maxTotalFruits(fruits: Array<IntArray>, startPos: Int, k: Int): Int {
        var n: Int = fruits.size
        var pref: IntArray = IntArray(n + 1), pos = IntArray(n)
        for (i in 0 until n) {
            pos[i] = fruits[i][0]
            pref[i + 1] = pref[i] + fruits[i][1]
        }
        var ans: Int = 0, j = 0
        for (i in 0 until n) {
            while (j < n && minSteps(pos[i], pos[j], startPos) > k) j++
            if (j <= i) ans = maxOf(ans, pref[i + 1] - pref[j])
        }
        j = 0
        for (i in 0 until n) {
            while (j <= i && minSteps(pos[j], pos[i], startPos) > k) j++
            ans = maxOf(ans, pref[i + 1] - pref[j])
        }
        return ans
    }
}
