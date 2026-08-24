struct Solution;
// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

impl Solution {
    pub fn max_increasing_subarrays(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut up = vec![0; n];
        up[n - 1] = 1;
        for i in (0..n - 1).rev() {
            up[i] = if nums[i] < nums[i + 1] { up[i + 1] + 1 } else { 1 };
        }
        let mut lo = 1;
        let mut hi = n / 2;
        let ok = |k: usize| -> bool {
            let mut i = 0;
            while i + 2 * k <= n {
                if up[i] >= k as i32 && up[i + k] >= k as i32 {
                    return true;
                }
                i += 1;
            }
            false
        };
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if ok(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}

fn main() {}
