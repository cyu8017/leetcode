// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

class Solution {
    func waysToBuyPensPencils(_ total: Int, _ cost1: Int, _ cost2: Int) -> Int {
        var ans = 0
        var pens = 0
        while pens * cost1 <= total {
            let remain = total - pens * cost1
            ans += remain / cost2 + 1
            pens += 1
        }
        return ans
    }
}
