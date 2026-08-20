// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

class Solution {
    func rangeSum(_ nums: [Int], _ n: Int, _ left: Int, _ right: Int) -> Int {
        var values = [Int]()
        for i in 0..<n {
            var total = 0
            for j in i..<n {
                total += nums[j]
                values.append(total)
            }
        }
        values.sort()
        var sum = 0
        for i in (left - 1)..<right {
            sum += values[i]
        }
        return sum % 1_000_000_007
    }
}
