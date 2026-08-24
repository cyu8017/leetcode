// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution {
    fun numSpecialEquivGroups(words: Array<String>): Int {
        var groups = HashSet()
        for (w in words) {
            var even = CharArray((w.size + 1) / 2)
            var odd = CharArray(w.size / 2)
            var ei = 0
            var oi = 0
            for (i in 0 until w.size) {
                if (i % 2 == 0) even[ei++] = w[i]
                else odd[oi++] = w[i]
            }
            even.sort()
            odd.sort()
            groups.add(String(even) + "|" + String(odd))
        }
        return groups.size
    }
}
