// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution {
    func numOfSubarrays(_ arr: [Int]) -> Int {
        var counts = [1, 0]
        var parity = 0, answer = 0
        for value in arr {
            parity ^= value & 1
            answer += counts[parity ^ 1]
            counts[parity] += 1
        }
        return answer % 1_000_000_007
    }
}
