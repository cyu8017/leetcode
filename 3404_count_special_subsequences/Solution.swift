// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

class Solution {
    func numberOfSubsequences(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            for j in (i + 2)..<n {
                for k in (j + 2)..<n {
                    for l in (k + 2)..<n {
                        if nums[i] * nums[k] == nums[j] * nums[l] { ans += 1 }
                    }
                }
            }
        }
        return ans
    }
}
