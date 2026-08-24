// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

class Solution {
    fun countValidSelections(nums: IntArray): Int {
        val n = nums.size
        var ans = 0
        for (i in 0 until n) {
            if (nums[i] != 0) continue
            for (dir in intArrayOf(-1, 1)) {
                val a = nums.clone()
                var cur = i
                var d = dir
                while (cur in 0 until n) {
                    if (a[cur] == 0) cur += d
                    else {
                        a[cur] = a[cur] - 1
                        d = -d
                        cur += d
                    }
                }
                var ok = true
                for (v in a) {
                    if (v != 0) {
                        ok = false
                        break
                    }
                }
                if (ok) ans++
            }
        }
        return ans
    }
}
