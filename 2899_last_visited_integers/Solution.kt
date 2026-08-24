// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

class Solution {
    fun lastVisitedIntegers(nums: IntArray): MutableList<Int> {
        var seen = ArrayList<Int>()
        var ans = ArrayList<Int>()
        var k = 0
        for (v in nums) {
            if (v != -1) {
                seen.add(v)
                k = 0
            } else {
                k++
                if (k > seen.size) ans.add(-1)
                else ans.add(seen[seen.size - k])
            }
        }
        return ans
    }
}
