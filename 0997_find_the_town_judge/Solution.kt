// LeetCode 0997 - Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/

class Solution {
    fun findJudge(n: Int, trust: Array<IntArray>): Int {
var score: IntArray = IntArray(n + 1)
for (t in trust) {
score[t[0]]--
score[t[1]]++
}
for (i in 1 ..n) {
if (score[i] == n - 1) {
return i
}
}
return -1
}
}
