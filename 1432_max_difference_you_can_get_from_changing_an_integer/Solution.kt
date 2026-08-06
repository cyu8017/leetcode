// LeetCode 1432 - Max Difference You Can Get From Changing an Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution {
    fun maxDiff(num: Int): Int {
        val s = num.toString()
        var high = s
        for (char in s) {
            if (char != '9') {
                high = s.replace(char, '9')
                break
            }
        }
        var low = s
        if (s[0] != '1') {
            low = s.replace(s[0], '1')
        } else {
            for (char in s.drop(1)) {
                if (char !in "01") {
                    low = s.replace(char, '0')
                    break
                }
            }
        }
        return high.toInt() - low.toInt()
    }
}
