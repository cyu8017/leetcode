// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution {
    func sumEvenAfterQueries(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        var nums = nums
        var even = nums.filter { $0 % 2 == 0 }.reduce(0, +)
        var ans = [Int](repeating: 0, count: queries.count)
        for (qi, q) in queries.enumerated() {
            let val = q[0], i = q[1]
            if nums[i] % 2 == 0 { even -= nums[i] }
            nums[i] += val
            if nums[i] % 2 == 0 { even += nums[i] }
            ans[qi] = even
        }
        return ans
    }
}
