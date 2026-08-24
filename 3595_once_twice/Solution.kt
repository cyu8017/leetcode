// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

class Solution {
    fun onceTwice(nums: IntArray): IntArray {
        var freq = HashMap<Int, Int>()
        for (x in nums) {
            if (!freq.containsKey(x)) freq[x] = 0
            freq[x] = freq[x] + 1
        }
        var a = 0
        var b = 0
        for (kv in freq) {
            if (kv.value == 1) a = kv.key
            else if (kv.value == 2) b = kv.key
        }
        return intArrayOf( a, b )
    }
}
