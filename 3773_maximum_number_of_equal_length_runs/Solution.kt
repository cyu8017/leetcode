// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

class Solution {
    fun maxSameLengthRuns(s: String): Int {
        var cnt = HashMap<Int, Int>()
        var n = s.length
        var ans = 0
        var i = 0
        while (i < n) {
            var j = i + 1
            while (j < n && s[j] == s[i]) { j += 1 }
            var m = j - i
            if (!cnt.containsKey(m)) cnt[m] = 0
            cnt[m] = cnt.getOrDefault(m, 0) + 1
            ans = maxOf(ans, cnt[m])
            i = j
            
        }
        return ans
    }
}
