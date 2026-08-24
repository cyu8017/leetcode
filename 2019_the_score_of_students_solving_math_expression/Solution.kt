// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

class Solution {
    private lateinit var s: String
    private lateinit var dp: Array<Array<HashSet<Int>>>

    private fun evalCorrect(s: String): Int {
var nums: MutableList<Int> = mutableListOf()
var ops: MutableList<Char> = mutableListOf()
for (char c : s.toCharArray()) {
if (c >= '0' && c <= '9') {
nums.add(c - '0')
}
else {
ops.add(c)
}
}
var newNums: MutableList<Int> = mutableListOf()
newNums.add(nums[0])
var newOps: MutableList<Char> = mutableListOf()
for (j in 0 until ops.size) {
if (ops[j] == '*') {
newNums.set(newNums.size - 1, newNums[newNums.size - 1] * nums[j + 1])
}
else {
newOps.add(ops[j])
newNums.add(nums[j + 1])
}
}
var res: Int = newNums[0]
for (j in 0 until newOps.size) {
res += newNums[j + 1]
}
return res
}

    fun scoreOfStudents(s: String, answers: IntArray): Int {
this.s = s
var n: Int = s.length
var correct: Int = evalCorrect(s)
dp = new HashSet[n][n]
var possible: HashSet<Int> = dfs(0, n - 1)
var ans: Int = 0
for (a in answers) {
if (a == correct) {
ans += 5
}
else if (possible.contains(a)) {
ans += 2
}
}
return ans
}

    private fun dfs(l: Int, r: Int): HashSet<Int> {
if (dp[l][r] != null) {
return dp[l][r]
}
var res: HashSet<Int> = HashSet()
if (l == r) {
res.add(s[l] - '0')
dp[l][r] = res
return res
}
/*for*/ var i = l + 1; while (i < r) {
for (a in dfs(l, i - 1)) {
for (b in dfs(i + 1, r)) {
var v: Int = if (s[i] == '+') a + b else a * b
if (v <= 1000) {
res.add(v)
}
}
}
}
dp[l][r] = res
return res
}
}
