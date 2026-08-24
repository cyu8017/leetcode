// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

class Solution {
    func xorAfterQueries(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let mod = 1_000_000_007
        var nums = nums
        for q in queries {
            let l = q[0], r = q[1], k = q[2], v = q[3]
            var idx = l
            while idx <= r {
                nums[idx] = nums[idx] * v % mod
                idx += k
            }
        }
        var ans = 0
        for x in nums { ans ^= x }
        return ans
    }
}
