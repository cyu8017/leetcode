// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

class Solution {
    func mostFrequentEven(_ nums: [Int]) -> Int {
        var cnt: [Int: Int] = [:]
        var ans = -1, best = 0
        for x in nums where x % 2 == 0 {
            cnt[x, default: 0] += 1
            let c = cnt[x]!
            if c > best || (c == best && (ans == -1 || x < ans)) {
                best = c
                ans = x
            }
        }
        return ans
    }
}
