// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution {
    func distinctDifferenceArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var suf = Array(repeating: 0, count: n + 1)
        var seen = Set<Int>()
        for i in stride(from: n - 1, through: 0, by: -1) {
            seen.insert(nums[i])
            suf[i] = seen.count
        }
        seen.removeAll()
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n {
            seen.insert(nums[i])
            ans[i] = seen.count - suf[i + 1]
        }
        return ans
    }
}
