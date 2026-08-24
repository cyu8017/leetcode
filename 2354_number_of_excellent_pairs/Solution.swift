// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

class Solution {
    func countExcellentPairs(_ nums: [Int], _ k: Int) -> Int {
        let uniq = Set(nums)
        var cnt = [Int](repeating: 0, count: 32)
        for x in uniq { cnt[x.nonzeroBitCount] += 1 }
        var ans = 0
        for i in 0..<32 {
            for j in 0..<32 where i + j >= k {
                ans += cnt[i] * cnt[j]
            }
        }
        return ans
    }
}
