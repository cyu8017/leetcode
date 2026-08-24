// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution {

    fun largestInteger(num: Int): Int {

            var digits = ArrayList<Int>()
            run { var x = num; while (x > 0) { digits.add(0, x % 10); x /= 10 } }
            var even = ArrayList<Int>()
            var odd = ArrayList<Int>()
            for (d in digits) {
                if (d % 2 == 0) even.add(d)
                else odd.add(d)
            }
            even.sort(Collections.reverseOrder())
            odd.sort(Collections.reverseOrder())
            var ei = 0; var oi = 0; var ans = 0
            for (d in digits) {
                if (d % 2 == 0) ans = ans * 10 + even[ei++]
                else ans = ans * 10 + odd[oi++]
            }
            return ans

    }

}
