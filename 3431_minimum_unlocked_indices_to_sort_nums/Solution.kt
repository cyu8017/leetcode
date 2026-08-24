// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

class Solution {
    fun minUnlockedIndices(nums: IntArray, locked: IntArray): Int {
        var n = nums.size
        var need = false
        for (i in 1 until n) {
            if (nums[i] < nums[i - 1]) { need = true; break; }
        }
        if (!need) return 0
        var left = n
        var right = -1
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (nums[i] > nums[j]) {
                    if (i < left) left = i
                    if (j > right) right = j
                }
            }
        }
        if (right < left) return 0
        var ans = 0
        for (i in left .. right) { if (locked[i] == 1) ans++ }
        var tmp = nums.clone()
        var lock = locked.clone()
        for (i in left .. right) { lock[i] = 0 }
        var changed = true
        while (changed) {
            changed = false
            var i = 0
            while (i + 1 < n) {
                if (lock[i] == 0 && lock[i + 1] == 0 && tmp[i] > tmp[i + 1]) {
                    var t = tmp[i]; tmp[i] = tmp[i + 1]; tmp[i + 1] = t
                    changed = true
                }
                i = i + 1
            }
        }
        for (i in 1 until n) { if (tmp[i] < tmp[i - 1]) return -1 }
        return ans
    }
}
