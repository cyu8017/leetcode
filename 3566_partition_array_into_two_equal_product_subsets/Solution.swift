// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

class Solution {
    func checkEqualPartitions(_ nums: [Int], _ target: Int) -> Bool {
        let n = nums.count
        for i in 0..<(1 << n) {
            var x = 1, y = 1
            var ok = true
            for j in 0..<n {
                if ((i >> j) & 1) != 0 { x *= nums[j] }
                else { y *= nums[j] }
                if x > target || y > target { ok = false; break }
            }
            if ok && x == target && y == target { return true }
        }
        return false
    }
}
