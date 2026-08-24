// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

class Solution {
    func specialTriplets(_ nums: [Int]) -> Int {
        var left = [Int: Int]()
        var right = [Int: Int]()
        for x in nums { right[x, default: 0] += 1 }
        var ans = 0
        let mod = 1_000_000_007
        for x in nums {
            right[x, default: 0] -= 1
            let lv = left[x * 2] ?? 0
            let rv = right[x * 2] ?? 0
            ans = (ans + lv * rv % mod) % mod
            left[x, default: 0] += 1
        }
        return ans
    }
}
