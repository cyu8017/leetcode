// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

class Solution {
    fun partitionString(s: String): MutableList<String> {
        var vis = HashSet<Int>()
        var ans = ArrayList<Int>()
        var t = StringBuilder()
        for (c in s.toCharArray()) {
            t.append(c)
            var cur = t.toString()
            if (!vis.contains(cur)) {
                vis.add(cur)
                ans.add(cur)
                t.setLength(0)
            }
        }
        return ans
    }
}
