// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

class Solution {
    fun findMissingElements(nums: IntArray): IntArray {
        var mn = 100
        var mx = 0
        var s = HashSet<Int>()
        for (x in nums) {
            mn = minOf(mn, x)
            mx = maxOf(mx, x)
            s.add(x)
        }
        var ans = ArrayList<Int>()
        for (x in mn + 1 until mx) {
            if (!s.contains(x)) ans.add(x)
        }
        return ans.toIntArray()
    }
}
