// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

class Solution {
    func minimumPossibleSum(_ n: Int, _ target: Int) -> Int {
        let mod = 1_000_000_007
        let m = target / 2
        if n <= m {
            return (n * (n + 1) / 2) % mod
        }
        var sum = m * (m + 1) / 2
        let remain = n - m
        sum += remain * target + remain * (remain - 1) / 2
        return sum % mod
    }
}
