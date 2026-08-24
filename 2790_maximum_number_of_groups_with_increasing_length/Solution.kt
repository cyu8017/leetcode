// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

class Solution {
    fun maxIncreasingGroups(usageLimits: MutableList<Int>): Int {
        var arr = IntArray(usageLimits.size)
        for (i in 0 until usageLimits.size) { arr[i] = usageLimits[i] }
        arr.sort()
        var ans = 0
        var sum = 0
        for (v in arr) {
            sum += v
            var need = 1L * (ans + 1) * (ans + 2) / 2
            if (sum >= need) ans++
        }
        return ans
    }
}
