// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var ans = 1 << 62
        if n < k { return 0 }
        for i in 0...(n - k) {
            var sub = Array(nums[i..<(i + k)])
            sub.sort()
            let med = sub[k / 2]
            var cost = 0
            for x in sub { cost += abs(x - med) }
            if cost < ans { ans = cost }
        }
        return ans
    }
}
