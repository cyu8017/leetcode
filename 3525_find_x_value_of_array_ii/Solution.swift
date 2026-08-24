// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

class Solution {
    func resultArray(_ nums: [Int], _ k: Int, _ queries: [[Int]]) -> [Int] {
        var nums = nums
        var ans = Array(repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let idx = queries[qi][0], val = queries[qi][1], start = queries[qi][2], x = queries[qi][3]
            nums[idx] = val
            var prod = 1, cnt = 0
            for i in start..<nums.count {
                prod = prod * (nums[i] % k) % k
                if prod == x { cnt += 1 }
            }
            ans[qi] = cnt
        }
        return ans
    }
}
