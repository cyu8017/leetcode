// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

class Solution {
    fun recoverArray(nums: IntArray): IntArray {
        nums.sort()
        var n: Int = nums.size
        for (i in 1 until n) {
            var diff: Int = nums[i] - nums[0]
            if (diff == 0 || diff % 2 != 0) continue
            var k: Int = diff / 2
            var used: BooleanArray = BooleanArray(n)
            used[0] = used[i] = true
            var ans = mutableListOf()
            ans.add((nums[0] + nums[i]) / 2)
            var l: Int = 0, r = i
            var ok: Boolean = true
            while (ans.size < n / 2) {
                while (l < n && used[l]) l++
                if (l == n) { ok = false; break; }
                var need: Int = nums[l] + 2 * k
                while (r < n && (used[r] || nums[r] < need)) r++
                if (r == n || nums[r] != need) { ok = false; break; }
                used[l] = used[r] = true
                ans.add(nums[l] + k)
            }
            if (ok) {
                var res: IntArray = IntArray(ans.size)
                for (t in 0 until ans.size) res[t] = ans.get(t)
                return res
            }
        }
        return IntArray(0)
    }
}
