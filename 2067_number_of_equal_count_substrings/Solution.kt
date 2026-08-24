// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

class Solution {
    fun equalCountSubstrings(s: String, count: Int): Int {
var ans: Int = 0, n = s.length
var seen: BooleanArray = BooleanArray(26)
var maxUnique: Int = 0
for (char c : s.toCharArray()) {
if (!seen[c - 'a']) {
seen[c - 'a'] = true
maxUnique++
}
}
for (u in 1 ..maxUnique) {
var needLen: Int = u * count
if (needLen > n) {
break
}
var freq: IntArray = IntArray(26)
var have: Int = 0
for (i in 0 until n) {
var c: Int = s[i] - 'a'
freq[c]++
if (freq[c] == count) {
have++
}
else if (freq[c] == count + 1) {
have--
}
if (i >= needLen) {
var p: Int = s[i - needLen] - 'a'
if (freq[p] == count) {
have--
}
else if (freq[p] == count + 1) {
have++
}
freq[p]--
}
if (i + 1 >= needLen && have == u) {
ans++
}
}
}
return ans
}
}
