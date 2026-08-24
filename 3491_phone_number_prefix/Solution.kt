// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

class Solution {
    fun phonePrefix(numbers: Array<String>): Boolean {
        numbers.sort()
        var i = 0
        while (i + 1 < numbers.size) {
            if (numbers[i].length <= numbers[i + 1].length
                    && numbers[i + 1].startsWith(numbers[i]))
                return false
            i = i + 1
        }
        return true
    }
}
