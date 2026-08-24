// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution {
    func sortArrayByParityII(_ nums: [Int]) -> [Int] {
        var ans = Array(repeating: 0, count: nums.count)
        var even = 0, odd = 1
        for x in nums {
            if x % 2 == 0 { ans[even] = x; even += 2 }
            else { ans[odd] = x; odd += 2 }
        }
        return ans
    }
}
