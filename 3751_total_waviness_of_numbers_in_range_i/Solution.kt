// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution {
    fun F(x: Int): Int {
        var nums = ArrayList<Int>()
        while (x > 0) {
            nums.add(x % 10)
            x /= 10
        }
        var m = nums.size
        if (m < 3) return 0
        var s = 0
        for (i in 1 until m - 1) {
            if ((nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ||
                (nums[i] < nums[i - 1] && nums[i] < nums[i + 1])) { s = s + 1 }
        }
        return s
    }

    fun totalWaviness(num1: Int, num2: Int): Int {
        var ans = 0
        for (x in num1 ..num2) { ans += F(x) }
        return ans
    }
}
