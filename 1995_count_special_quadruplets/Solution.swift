// LeetCode 1995 - Count Special Quadruplets
// https://leetcode.com/problems/count-special-quadruplets/

class Solution {
    func countQuadruplets(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for a in 0..<n {
            for b in (a + 1)..<n {
                for c in (b + 1)..<n {
                    let s = nums[a] + nums[b] + nums[c]
                    for d in (c + 1)..<n where nums[d] == s {
                        ans += 1
                    }
                }
            }
        }
        return ans
    }
}
