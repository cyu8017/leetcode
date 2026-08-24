// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution {
    fun findArray(pref: IntArray): IntArray {
            var ans: IntArray = IntArray(pref.size)
            ans[0] = pref[0]
            var i: Int = 1
    while (i < pref.size) {
    
                ans[i] = pref[i] ^ pref[i - 1]
    i = i + 1
    }
            return ans
    }
}
