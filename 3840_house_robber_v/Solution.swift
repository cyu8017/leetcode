// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

class Solution {
    func rob(_ nums: [Int], _ colors: [Int]) -> Int {
        let n = nums.count
        var f = 0, g = nums[0]
        if n > 1 {
            for i in 1..<n {
                if colors[i - 1] == colors[i] {
                    let nf = max(f, g)
                    g = f + nums[i]
                    f = nf
                } else {
                    let nf = max(f, g)
                    g = nf + nums[i]
                    f = nf
                }
            }
        }
        return max(f, g)
    }
}
