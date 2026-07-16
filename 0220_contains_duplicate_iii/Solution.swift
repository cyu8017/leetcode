// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

class Solution {
    func containsNearbyAlmostDuplicate(_ nums: [Int], _ indexDiff: Int, _ valueDiff: Int) -> Bool {
        if indexDiff <= 0 || valueDiff < 0 {
            return false
        }
        let width = Int64(valueDiff) + 1
        var buckets = [Int64: Int64]()

        func bucketId(_ num: Int64) -> Int64 {
            num >= 0 ? num / width : (num + 1) / width - 1
        }

        for i in nums.indices {
            let num = Int64(nums[i])
            let bucket = bucketId(num)
            if buckets[bucket] != nil {
                return true
            }
            if let prev = buckets[bucket - 1], abs(num - prev) <= Int64(valueDiff) {
                return true
            }
            if let prev = buckets[bucket + 1], abs(num - prev) <= Int64(valueDiff) {
                return true
            }
            if buckets.count >= indexDiff {
                buckets.removeValue(forKey: bucketId(Int64(nums[i - indexDiff])))
            }
            buckets[bucket] = num
        }
        return false
    }
}
