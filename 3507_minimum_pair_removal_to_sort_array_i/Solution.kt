// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

class Solution {
    private fun isNonDecreasing(a: MutableList<Int>): Boolean {
        for (i in 1 until a.size) { if (a[i] < a[i - 1]) return false }
        return true
    }
    fun minimumPairRemoval(nums: IntArray): Int {
        var arr = ArrayList<Int>()
        for (x in nums) { arr.add(x) }
        var ans = 0
        while (!isNonDecreasing(arr)) {
            var k = 0
            var s = arr[0] + arr[1]
            var i = 1
            while (i + 1 < arr.size) {
                var t = arr[i] + arr[i + 1]
                if (s > t) { s = t; k = i; }
                i = i + 1
            }
            arr.set(k, s)
            arr.remove(k + 1)
            ans = ans + 1
        }
        return ans
    }
}
