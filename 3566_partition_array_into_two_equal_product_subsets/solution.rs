// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

impl Solution {
    pub fn check_equal_partitions(nums: Vec<i32>, target: i64) -> bool {
        let n = nums.len();
        for i in 0..(1 << n) {
            let mut x = 1i64;
            let mut y = 1i64;
            let mut ok = true;
            for j in 0..n {
                if (i >> j) & 1 == 1 {
                    x *= nums[j] as i64;
                } else {
                    y *= nums[j] as i64;
                }
                if x > target || y > target {
                    ok = false;
                    break;
                }
            }
            if ok && x == target && y == target {
                return true;
            }
        }
        false
    }
}
