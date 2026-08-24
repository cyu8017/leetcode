// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

class Solution {
    fun findCommonResponse(responses: MutableList<MutableList<String>>): String {
        var cnt = HashMap<String, Int>()
        for (ws in responses) {
            var s = HashSet<String>()
            for (w in ws) {
                if (s.add(w)) cnt.merge(w, 1, Integer::sum)
            }
        }
        var ans = responses[0][0]
        for (e in cnt) {
            var w = e.key
            var v = e.value
            if (cnt[ans] < v || (cnt[ans] == v && w.compareTo(ans) < 0)) ans = w
        }
        return ans
    }
}
