// LeetCode 1432 - Max Difference You Can Get From Changing an Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution {
    fun maxDiff(num: Int): Int {
        val s = num.toString()
        var high = s
        for (ch in s) {
            if (ch != '9') {
                high = s.replace(ch, '9')
                break
            }
        }
        var low = s
        if (s[0] != '1') {
            low = s.replace(s[0], '1')
        } else {
            for (ch in s.substring(1)) {
                if (ch != '0' && ch != '1') {
                    low = s.replace(ch, '0')
                    break
                }
            }
        }
        return high.toInt() - low.toInt()
    }
}
