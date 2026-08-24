// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution {
    func averageValue(_ nums: [Int]) -> Int {
        var sum = 0, cnt = 0
        for x in nums where x % 6 == 0 {
            sum += x
            cnt += 1
        }
        return cnt == 0 ? 0 : sum / cnt
    }
}
