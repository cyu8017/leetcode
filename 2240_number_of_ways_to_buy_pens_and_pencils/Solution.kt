// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

class Solution {

    fun waysToBuyPensPencils(total: Int, cost1: Int, cost2: Int): Long {

            var ans = 0
            run {
    var pens = 0
    while (pens * cost1 <= total) {

                var remain = total - pens * cost1
                ans += remain / cost2 + 1

    pens++
    }
    }
            return ans

    }

}
