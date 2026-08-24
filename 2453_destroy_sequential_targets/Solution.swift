// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

class Solution {
    func destroyTargets(_ nums: [Int], _ space: Int) -> Int {
        var cnt = [Int: Int]()
        for x in nums { cnt[x % space, default: 0] += 1 }
        let bestCnt = cnt.values.max() ?? 0
        var ans = Int.max
        for x in nums {
            if cnt[x % space] == bestCnt { ans = min(ans, x) }
        }
        return ans
    }
}
