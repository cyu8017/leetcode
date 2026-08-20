// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution {
    func minSubarray(_ nums: [Int], _ p: Int) -> Int {
        let target = nums.reduce(0, +) % p
        if target == 0 { return 0 }
        var seen = [0: -1]
        var prefix = 0, answer = nums.count
        for (i, x) in nums.enumerated() {
            prefix = (prefix + x) % p
            let need = (prefix - target + p) % p
            if let j = seen[need] {
                answer = min(answer, i - j)
            }
            seen[prefix] = i
        }
        return answer < nums.count ? answer : -1
    }
}
