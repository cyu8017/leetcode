// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution {
    func prefixesDivBy5(_ nums: [Int]) -> [Bool] {
        var ans = [Bool]()
        var rem = 0
        for bit in nums {
            rem = (rem * 2 + bit) % 5
            ans.append(rem == 0)
        }
        return ans
    }
}
