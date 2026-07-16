// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

use std::collections::HashMap;

impl Solution {
    pub fn contains_nearby_almost_duplicate(
        nums: Vec<i32>,
        index_diff: i32,
        value_diff: i32,
    ) -> bool {
        if index_diff <= 0 || value_diff < 0 {
            return false;
        }
        let width = value_diff as i64 + 1;
        let mut buckets: HashMap<i64, i64> = HashMap::new();

        fn bucket_id(num: i64, width: i64) -> i64 {
            if num >= 0 {
                num / width
            } else {
                (num + 1) / width - 1
            }
        }

        for (i, num) in nums.iter().enumerate() {
            let num = *num as i64;
            let bucket = bucket_id(num, width);
            if buckets.contains_key(&bucket) {
                return true;
            }
            if buckets.get(&(bucket - 1)).map_or(false, |prev| (num - prev).abs() <= value_diff as i64) {
                return true;
            }
            if buckets.get(&(bucket + 1)).map_or(false, |next| (num - next).abs() <= value_diff as i64) {
                return true;
            }
            if buckets.len() as i32 >= index_diff {
                let old = nums[i - index_diff as usize] as i64;
                buckets.remove(&bucket_id(old, width));
            }
            buckets.insert(bucket, num);
        }
        false
    }
}
