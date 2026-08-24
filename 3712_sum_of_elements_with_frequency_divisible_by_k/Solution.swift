// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

class Solution {
    func sumDivisibleByK(_ nums: [Int], _ k: Int) -> Int {
        var cnt = [Int: Int]()
        for x in nums { cnt[x, default: 0] += 1 }
        var ans = 0
        for (k0, v) in cnt {
            if v % k == 0 { ans += k0 * v }
        }
        return ans
    }
}
