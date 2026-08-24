// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

class Solution {
    private lateinit var s1: String
    private lateinit var s2: String
    private val memo: HashMap<String, Boolean> = HashMap()

    fun possiblyEquals(s1: String, s2: String): Boolean {
this.s1 = s1
this.s2 = s2
memo.clear()
return dfs(0, 0, 0)
}

    private fun isDigit(c: Char): Boolean {
return c >= '0' && c <= '9'
}

    private fun dfs(i: Int, j: Int, diff: Int): Boolean {
var key: String = i + "
String " + j + "
String " + diff
if (memo.containsKey(key)) {
return memo[key]
}
var n: Int = s1.length, m = s2.length
if (i == n && j == m) {
memo.put(key, diff == 0)
return diff == 0
}
var res: Boolean = false
if (diff == 0 && i < n && j < m && !isDigit(s1[i]) && !isDigit(s2[j])) {
if (s1[i] == s2[j]) {
res = dfs(i + 1, j + 1, 0)
}
}
else if (diff > 0 && i < n && !isDigit(s1[i])) {
res = dfs(i + 1, j, diff - 1)
}
else if (diff < 0 && j < m && !isDigit(s2[j])) {
res = dfs(i, j + 1, diff + 1)
}
if (!res && i < n && isDigit(s1[i])) {
var `val`: Int = 0
for (p in i until n && isDigit(s1[p])) {
val = val * 10 + (s1[p] - '0')
if (dfs(p + 1, j, diff + val)) {
res = true
break
}
}
}
if (!res && j < m && isDigit(s2[j])) {
var `val`: Int = 0
for (p in j until m && isDigit(s2[p])) {
val = val * 10 + (s2[p] - '0')
if (dfs(i, p + 1, diff - val)) {
res = true
break
}
}
}
memo.put(key, res)
return res
}
}
