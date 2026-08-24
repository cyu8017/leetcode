// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution {
    fun nextBeautifulNumber(n: Int): Int {
/*for*/ var x = n + 1; while () {
if (balanced(x)) {
return x
}
}
}

    private fun balanced(x: Int): Boolean {
var cnt: IntArray = IntArray(10)
while (x > 0) {
cnt[x % 10]++
x /= 10
}
for (d in 0 until 10) {
if (cnt[d] != 0 && cnt[d] != d) {
return false
}
}
return true
}
}
