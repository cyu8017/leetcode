// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

impl Solution {
    pub fn min_size_subarray(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let total: i64 = nums.iter().map(|&v| v as i64).sum();
        let mut ans = 1 << 30;
        if total > 0 {
            let loops = target as i64 / total;
            let remain = (target as i64 % total) as i32;
            if remain == 0 {
                return (loops * n as i64) as i32;
            }
            let mut arr = nums.clone();
            arr.extend_from_slice(&nums);
            let mut left = 0usize;
            let mut sum = 0i32;
            let mut best = 1 << 30;
            for right in 0..arr.len() {
                sum += arr[right];
                while sum > remain && left <= right {
                    sum -= arr[left];
                    left += 1;
                }
                if sum == remain && ((right - left + 1) as i32) < best {
                    best = (right - left + 1) as i32;
                }
            }
            if best < (1 << 30) {
                ans = (loops * n as i64) as i32 + best;
            }
        }
        if ans == (1 << 30) { -1 } else { ans }
    }
}
