// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

class Solution {
    fun numRookCaptures(board: Array<CharArray>): Int {
var m: Int = board.size
var n: Int = board[0].size
var r: Int = -1
var c: Int = -1
for (i in 0 until m) {
for (j in 0 until n) {
if (board[i][j] == 'R') {
r = i
c = j
}
}
}
if (r < 0) {
return 0
}
var ans: Int = 0
var dirs: Array<IntArray> = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
for (d in dirs) {
var i: Int = r + d[0]
var j: Int = c + d[1]
while (i >= 0 && i < m && j >= 0 && j < n) {
if (board[i][j] == 'B') {
break
}
if (board[i][j] == 'p') {
ans++
break
}
i += d[0]
j += d[1]
}
}
return ans
}
}
