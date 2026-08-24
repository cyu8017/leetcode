// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

class Solution {

    fun largestVariance(s: String): Int {

            var ans = 0
            run {
    var a = 'a'
    while (a <= 'z') {

                run {
    var b = 'a'
    while (b <= 'z') {

                    if (a == b) continue
                    var bal = 0
                    var hasB = false
                    for (c in s.toCharArray()) {
                        if (c == a) bal++
                        else if (c == b) { bal--; hasB = true; }
                        if (hasB) ans = maxOf(ans, bal)
                        if (bal < 0) { bal = 0; hasB = false; }
                    }

    b++
    }
    }

    a++
    }
    }
            return ans

    }

}
