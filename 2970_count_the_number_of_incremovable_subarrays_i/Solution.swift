// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

class Solution {
    func incremovableSubarrayCount(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            for j in i..<n {
                var prev = -1
                var ok = true
                for t in 0..<n {
                    if t >= i && t <= j { continue }
                    if nums[t] <= prev {
                        ok = false
                        break
                    }
                    prev = nums[t]
                }
                if ok { ans += 1 }
            }
        }
        return ans
    }
}
