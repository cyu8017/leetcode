// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

class Solution {
    func makeParityAlternating(_ nums: [Int]) -> [Int] {
        if nums.count == 1 { return [0, 0] }
        var mn = nums[0], mx = nums[0]
        for x in nums { mn = min(mn, x); mx = max(mx, x) }
        let r0 = f(nums, 0, mn, mx)
        let r1 = f(nums, 1, mn, mx)
        if r0[0] != r1[0] { return r0[0] < r1[0] ? r0 : r1 }
        return r0[1] <= r1[1] ? r0 : r1
    }

    private func f(_ nums: [Int], _ k: Int, _ mn: Int, _ mx: Int) -> [Int] {
        var cnt = 0, a = Int.max, b = Int.min
        for i in 0..<nums.count {
            var x = nums[i]
            if ((x - i) & 1) != k {
                cnt += 1
                if x == mn { x += 1 }
                else if x == mx { x -= 1 }
            }
            a = min(a, x)
            b = max(b, x)
        }
        return [cnt, max(1, b - a)]
    }
}
