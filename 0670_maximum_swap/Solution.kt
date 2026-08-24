// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/


class Solution {
    fun maximumSwap(num: Int): Int {
        val digits = num.toString().toCharArray()
        val last = IntArray(10) { -1 }
        for (i in digits.indices) last[digits[i] - '0'] = i
        for (i in digits.indices) {
            for (d in 9 downTo digits[i] - '0' + 1) {
                if (last[d] > i) {
                    val tmp = digits[i]
                    digits[i] = digits[last[d]]
                    digits[last[d]] = tmp
                    return String(digits).toInt()
                }
            }
        }
        return num
    }
}
