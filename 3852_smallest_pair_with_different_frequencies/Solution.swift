// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

class Solution {
    func minDistinctFreqPair(_ nums: [Int]) -> [Int] {
        var cnt = [Int: Int]()
        for v in nums { cnt[v, default: 0] += 1 }
        var x = nums[0]
        for v in nums { x = min(x, v) }
        var minY = Int.max
        for y in cnt.keys {
            if y < minY && cnt[x] != cnt[y] { minY = y }
        }
        if minY == Int.max { return [-1, -1] }
        return [x, minY]
    }
}
