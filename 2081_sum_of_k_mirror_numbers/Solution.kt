// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

class Solution {
    fun kMirror(k: Int, n: Int): Long {
var ans: Long = 0
var count: Int = 0
/*for*/ var length = 1; while (count < n) {
var start: Int = 1
for (i in 1 until (length + 1) / 2) {
start *= 10
}
var end: Int = start * 10
for (half in start until end && count < n) {
var pal: Long = half
if (length % 2 == 0) {
var x: Int = half
while (x > 0) {
pal = pal * 10 + x % 10
x /= 10
}
}
else {
var x: Int = half / 10
while (x > 0) {
pal = pal * 10 + x % 10
x /= 10
}
}
if (isPalBase(pal, k)) {
ans += pal
count++
}
}
}
return ans
}

    private fun isPalBase(x: Long, bas: Int): Boolean {
var digits: MutableList<Int> = mutableListOf()
while (x > 0) {
digits.add((x % bas).toInt())
x /= bas
}
/*for*/ var l = 0, r = digits.size - 1; while (l < r) {
if (!digits[l].equals(digits[r])) {
return false
}
}
return true
}
}
