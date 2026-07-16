// LeetCode 0202 - Happy Number\n// https://leetcode.com/problems/\n\nclass Solution {
    fun isHappy(n: Int): Boolean {
        var value = n; val seen = mutableSetOf<Int>()
        while (value != 1 && seen.add(value)) value = nextValue(value)
        return value == 1
    }

    private fun nextValue(value: Int): Int {
        var number = value; var total = 0
        while (number > 0) { val digit = number % 10; total += digit * digit; number /= 10 }
        return total
    }
}
