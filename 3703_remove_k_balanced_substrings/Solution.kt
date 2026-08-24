// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

class Solution {
    fun removeSubstring(s: String, k: Int): String {
        var stk = ArrayList<IntArray>()
        for (c in s.toCharArray()) {
            if (!stk.isEmpty() && stk[stk.size(] - 1)[0] == c)
                stk[stk.size - 1][1]++
            else stk.add(intArrayOf(c, 1))
            if (c == ')' && stk.size > 1) {
                var top = stk[stk.size - 1]
                var prev = stk[stk.size - 2]
                if (top[1] == k && prev[1] >= k) {
                    stk.remove(stk.size - 1)
                    prev[1] -= k
                    if (prev[1] == 0) stk.remove(stk.size() - 1)
                }
            }
        }
        var res = StringBuilder()
        for (int[] p : stk)
            for (i in 0 until p[1]) { res.append((char) p[0]) }
        return res.toString()
    }
}
