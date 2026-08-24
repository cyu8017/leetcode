// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

class Solution {
    func perfectPairs(_ nums: [Int]) -> Int {
        let n = nums.count
        var absNums = nums.map { abs($0) }.sorted()
        var ans = 0, j = 0
        for i in 0..<n {
            if j < i + 1 { j = i + 1 }
            while j < n && absNums[j] <= 2 * absNums[i] { j += 1 }
            ans += j - i - 1
        }
        return ans
    }
}
