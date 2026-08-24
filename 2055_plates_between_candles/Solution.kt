// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

class Solution {
    fun platesBetweenCandles(s: String, queries: Array<IntArray>): IntArray {
var n: Int = s.length
var pref: IntArray = IntArray(n + 1)
var left: IntArray = IntArray(n)
var right: IntArray = IntArray(n)
var last: Int = -1
for (i in 0 until n) {
pref[i + 1] = pref[i] + (if (s[i] == '*') 1 else 0)
if (s[i] == '|') {
last = i
}
left[i] = last
}
last = -1
for (i in n - 1 downTo 0) {
if (s[i] == '|') {
last = i
}
right[i] = last
}
var ans: IntArray = IntArray(queries.size)
for (i in 0 until queries.size) {
var l: Int = right[queries[i][0]]
var r: Int = left[queries[i][1]]
if (l != -1 && r != -1 && l < r) {
ans[i] = pref[r] - pref[l]
}
}
return ans
}
}
