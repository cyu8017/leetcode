// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

class Solution {
    func smallestDistancePair(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        var lo = 0, hi = nums.last! - nums[0]
        while lo < hi {
            let mid = (lo + hi) / 2
            if count(nums, mid) >= k { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }

    private func count(_ nums: [Int], _ dist: Int) -> Int {
        var j = 0, cnt = 0
        for i in 0..<nums.count {
            while nums[i] - nums[j] > dist { j += 1 }
            cnt += i - j
        }
        return cnt
    }
}
