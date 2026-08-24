// LeetCode 2149 - Rearrange Array Elements by Sign
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution {
    func rearrangeArray(_ nums: [Int]) -> [Int] {
        var ans = [Int](repeating: 0, count: nums.count)
        var pos = 0, neg = 1
        for x in nums {
            if x > 0 { ans[pos] = x; pos += 2 }
            else { ans[neg] = x; neg += 2 }
        }
        return ans
    }
}
