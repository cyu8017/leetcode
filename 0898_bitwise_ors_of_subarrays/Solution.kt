// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

class Solution {
    fun subarrayBitwiseORs(arr: IntArray): Int {
        var ans = HashSet<Int>()
        var cur = HashSet<Int>()
        for (x in arr) {
            var nxt = HashSet<Int>()
            nxt.add(x)
            for (y in cur) { nxt.add(x | y); }
            cur = nxt
            ans.addAll(cur)
        }
        return ans.size
    }
}
