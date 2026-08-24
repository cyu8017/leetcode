// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

impl Solution {
    fn count_inv(nums: &[i32], k: i32, threshold: i32) -> bool {
        let mut sorted = Vec::new();
        let mut inv = 0i64;
        for &num in nums {
            let left = sorted.partition_point(|&x| x <= num);
            let right = sorted.partition_point(|&x| x <= num + threshold);
            inv += (right - left) as i64;
            let pos = sorted.partition_point(|&x| x <= num);
            sorted.insert(pos, num);
        }
        inv >= k as i64
    }

    pub fn min_threshold(nums: Vec<i32>, k: i32) -> i32 {
        let mx = *nums.iter().max().unwrap_or(&0);
        let mut l = 0;
        let mut r = mx + 1;
        while l < r {
            let m = (l + r) / 2;
            if Self::count_inv(&nums, k, m) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        if l > mx { -1 } else { l }
    }
}
