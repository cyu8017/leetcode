// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution {

    fun digitSum(s: String, k: Int): String {
        var _s = s

            while (_s.length > k) {
                var next = StringBuilder()
                run {
    var i = 0
    while (i < _s.length) {

                    var sum = 0
                    var end = minOf(i + k, _s.length)
                    for (j in i until end) { sum += _s[j] - '0' }
                    next.append(sum)

    i += k
    }
    }
                _s = next.toString()
            }
            return _s
    }

}
