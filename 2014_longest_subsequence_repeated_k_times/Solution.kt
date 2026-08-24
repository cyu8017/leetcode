// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

class Solution {
    fun longestSubsequenceRepeatedK(s: String, k: Int): String {
var freq: IntArray = IntArray(26)
for (char c : s.toCharArray()) {
freq[c - 'a']++
}
var chars: StringBuilder = StringBuilder()
for (c in 25 downTo 0) {
if (freq[c] >= k) {
chars.append((char) ('a' + c))
}
}
var best: String = ""
var q: ArrayDeque<String> = ArrayDeque()
q.add("")
while (!q.isEmpty()) {
var cur: String = q.removeFirst()
for (i in 0 until chars.size) {
var nxt: String = cur + chars[i]
if (isSubseq(s, nxt, k)) {
if (nxt.length > best.length || (nxt.length == best.length && nxt.compareTo(best) > 0)) {
best = nxt
}
q.add(nxt)
}
}
}
return best
}

    private fun isSubseq(s: String, t: String, k: Int): Boolean {
var need: Int = 0
var times: Int = 0
for (i in 0 until s.length) {
if (s[i] == t[need]) {
need++
if (need == t.length) {
times++
if (times == k) {
return true
}
need = 0
}
}
}
return false
}
}
