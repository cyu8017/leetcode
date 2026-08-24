// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution {
    fun minimumMoves(s: String): Int {
var ans: Int = 0
/*for*/ var i = 0; while (i < s.length) {
if (s[i] == 'X') {
ans++
i += 3
}
else {
i++
}
}
return ans
}
}
