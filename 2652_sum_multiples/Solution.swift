// LeetCode 2652 - Sum Multiples
// https://leetcode.com/problems/sum-multiples/

class Solution {
    func sumOfMultiples(_ n: Int) -> Int {
        var ans = 0
        for i in 1...n where i % 3 == 0 || i % 5 == 0 || i % 7 == 0 {
            ans += i
        }
        return ans
    }
}
