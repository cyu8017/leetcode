// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

class Solution {
    fun selfDividingNumbers(left: Int, right: Int): MutableList<Int> {
        var result = ArrayList<Int>()
        for (num in left ..right) { if (isSelfDividing(num)) result.add(num) }
        return result
    }

    private fun isSelfDividing(num: Int): Boolean {
        var x = num
        while (x > 0) {
            var digit = x % 10
            if (digit == 0 || num % digit != 0) return false
            x /= 10
        }
        return true
    }
}
