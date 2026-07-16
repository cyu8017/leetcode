// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

class Solution {
    func singleNumber(_ nums: [Int]) -> [Int] {
        var xorAll = 0
        for num in nums {
            xorAll ^= num
        }
        let diff = xorAll & -xorAll
        var first = 0
        var second = 0
        for num in nums {
            if num & diff != 0 {
                first ^= num
            } else {
                second ^= num
            }
        }
        return [first, second]
    }
}
