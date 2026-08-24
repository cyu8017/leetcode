// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

impl Solution {
    pub fn min_removal(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut cnt = 0;
        for i in 0..n {
            let mut j = n;
            if nums[i] as i64 * k as i64 <= nums[n - 1] as i64 {
                let target = nums[i] as i64 * k as i64 + 1;
                j = nums.partition_point(|&x| (x as i64) < target);
            }
            cnt = cnt.max(j - i);
        }
        (n - cnt) as i32
    }
}
