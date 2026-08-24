// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

class Solution {
    fun minimumCost(sentence: String, k: Int): Int {
var words: Array<String> = sentence.trim().split("\\s+")
var n: Int = words.size
var INF: Long = 1e18
var dp: LongArray = LongArray(n + 1)
dp.fill(INF)
dp[n] = 0
for (i in n - 1 downTo 0) {
var length: Int = -1
for (j in i until n) {
length += 1 + words[j].length
if (length > k) {
break
}
var cost: Long = 0
if (j < n - 1) {
var extra: Long = k - length
cost = extra * extra
}
dp[i] = minOf(dp[i], cost + dp[j + 1])
}
}
return dp.toInt()[0]
}
}
