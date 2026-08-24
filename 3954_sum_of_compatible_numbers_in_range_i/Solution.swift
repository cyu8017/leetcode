// LeetCode 3954 - Sum of Compatible Numbers in Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/


class Solution {
    func sumOfGoodIntegers(_ n: Int, _ k: Int) -> Int {
        let start = max(1, n - k)
        let end = n + k
        var ans = 0
        for x in start...end {
            if (n & x) == 0 { ans += x }
        }
        return ans
    }
}
