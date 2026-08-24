// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

class Solution {
    func minSwaps(_ nums: [Int]) -> Int {
        var pos = [[Int](), [Int]()]
        for i in 0..<nums.count { pos[nums[i] & 1].append(i) }
        if abs(pos[0].count - pos[1].count) > 1 { return -1 }
        if pos[0].count > pos[1].count { return calc(pos, nums.count, 0) }
        if pos[0].count < pos[1].count { return calc(pos, nums.count, 1) }
        return min(calc(pos, nums.count, 0), calc(pos, nums.count, 1))
    }

    func calc(_ pos: [[Int]], _ n: Int, _ k: Int) -> Int {
        var res = 0
        for i in stride(from: 0, to: n, by: 2) { res += abs(pos[k][i / 2] - i) }
        return res
    }
}
