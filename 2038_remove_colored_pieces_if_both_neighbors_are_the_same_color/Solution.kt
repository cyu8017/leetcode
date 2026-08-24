// LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution {
    fun winnerOfGame(colors: String): Boolean {
var a: Int = 0
var b: Int = 0
/*for*/ var i = 1; while (i + 1 < colors.length) {
if (colors[i - 1] == colors[i] && colors[i] == colors[i + 1]) {
if (colors[i] == 'A') {
a++
}
else {
b++
}
}
}
lateinit var b: return a >
}
}
