// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

impl Solution {
    pub fn can_three_parts_equal_sum(arr: Vec<i32>) -> bool {
        let total: i32 = arr.iter().sum();
        if total % 3 != 0 {
            return false;
        }
        let target = total / 3;
        let mut parts = 0;
        let mut cur = 0;
        for x in arr {
            cur += x;
            if cur == target {
                parts += 1;
                cur = 0;
            }
        }
        parts >= 3
    }
}
