// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

class Solution {
    fun placeWordInCrossword(board: Array<CharArray>, word: String): Boolean {
var m: Int = board.size, n = board[0].size, L = word.length
for (r in 0 until m) {
var c: Int = 0
while (c < n) {
while (c < n && board[r][c] == '#') {
c++
}
var start: Int = c
while (c < n && board[r][c] != '#') {
c++
}
if (c - start == L) {
var sb: StringBuilder = StringBuilder()
for (i in start until c) {
sb.append(board[r][i])
}
if (match(sb.toString(), word)) {
return true
}
}
}
}
for (c in 0 until n) {
var r: Int = 0
while (r < m) {
while (r < m && board[r][c] == '#') {
r++
}
var start: Int = r
while (r < m && board[r][c] != '#') {
r++
}
if (r - start == L) {
var sb: StringBuilder = StringBuilder()
for (i in 0 until L) {
sb.append(board[start + i][c])
}
if (match(sb.toString(), word)) {
return true
}
}
}
}
return false
}

    private fun match(cells: String, word: String): Boolean {
var L: Int = word.length
if (cells.length != L) {
return false
}
var ok1: Boolean = true
var ok2: Boolean = true
for (i in 0 until L) {
if (cells[i] != ' ' && cells[i] != word[i]) {
ok1 = false
}
if (cells[i] != ' ' && cells[i] != word[L - 1 - i]) {
ok2 = false
}
}
return ok1 || ok2
}
}
