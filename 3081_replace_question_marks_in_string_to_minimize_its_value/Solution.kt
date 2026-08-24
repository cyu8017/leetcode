// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

class Solution {
    fun minimizeStringValue(s: String): String {
        var cnt = IntArray(26)
        var k = 0
        for (i in 0 until s.length) {
            var c = s[i]
            if (c == '?') k++
            else cnt[c - 'a']++
        }
        var pq = PriorityQueue((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1])
        for (i in 0 until 26) { pq.offer(intArrayOf(cnt[i], i)) }
        var t = IntArray(k)
        for (i in 0 until k) {
            var p = pq.poll()
            t[i] = p[1]
            p[0]++
            pq.offer(p)
        }
        t.sort()
        var arr = s.toCharArray()
        var j = 0
        for (i in 0 until arr.size) {
            if (arr[i] == '?') {
                arr[i] = (char) (t[j] + 'a')
                j++
            }
        }
        return String(arr)
    }
}
