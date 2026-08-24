// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

class Solution {
    func duplicateNumbersXOR(_ nums: [Int]) -> Int {
        var cnt = Array(repeating: 0, count: 51)
        var ans = 0
        for x in nums {
            cnt[x] += 1
            if cnt[x] == 2 { ans ^= x }
        }
        return ans
    }
}
