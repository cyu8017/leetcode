// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

class Solution {
    func partitionArray(_ nums: [Int], _ k: Int) -> Bool {
        let n = nums.count
        if n % k != 0 { return false }
        let m = n / k
        var mx = 0
        for x in nums { mx = max(mx, x) }
        var cnt = Array(repeating: 0, count: mx + 1)
        for x in nums {
            cnt[x] += 1
            if cnt[x] > m { return false }
        }
        return true
    }
}
