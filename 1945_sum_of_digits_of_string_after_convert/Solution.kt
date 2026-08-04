// LeetCode 1945
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution {
    fun getLucky(s: String, k: Int): Int {
        var num = s.map { (it - 'a' + 1).toString() }.joinToString("")
        repeat(k) { num = num.sumOf { it - '0' }.toString() }
        return num.toInt()
    }
}
