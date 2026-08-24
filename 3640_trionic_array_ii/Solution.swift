// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

class Solution {
    func maxSumTrionic(_ nums: [Int]) -> Int {
        let n = nums.count
        var i = 0
        var ans = Int.min
        while i < n {
            let l = i
            i += 1
            while i < n && nums[i - 1] < nums[i] { i += 1 }
            if i == l + 1 { continue }
            let p = i - 1
            var s = nums[p - 1] + nums[p]
            while i < n && nums[i - 1] > nums[i] {
                s += nums[i]
                i += 1
            }
            if i == p + 1 || i == n || nums[i - 1] == nums[i] { continue }
            let q = i - 1
            s += nums[i]
            i += 1
            var mx = 0, t = 0
            while i < n && nums[i - 1] < nums[i] {
                t += nums[i]
                i += 1
                mx = max(mx, t)
            }
            s += mx
            mx = 0; t = 0
            if p - 2 >= l {
                for j in stride(from: p - 2, through: l, by: -1) {
                    t += nums[j]
                    mx = max(mx, t)
                }
            }
            s += mx
            ans = max(ans, s)
            i = q
        }
        return ans
    }
}
