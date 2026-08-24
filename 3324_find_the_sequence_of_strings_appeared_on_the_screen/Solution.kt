// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

class Solution {
    fun stringSequence(target: String): MutableList<String> {
        var ans = ArrayList<String>()
        var cur = StringBuilder()
        for (ch in target.toCharArray()) {
            cur.append('a')
            ans.add(cur.toString())
            while (cur[cur.length - 1] != ch) {
                cur.setCharAt(cur.length - 1, (char) (cur[cur.length - 1] + 1))
                ans.add(cur.toString())
            }
        }
        return ans
    }
}
