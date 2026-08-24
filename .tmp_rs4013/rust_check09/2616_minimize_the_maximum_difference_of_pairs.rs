struct Solution;

// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

impl Solution {
    pub fn minimize_max(mut nums: Vec<i32>, p: i32) -> i32 {
        nums.sort_unstable();
        let ok = |d: i32| {
            let mut cnt = 0;
            let mut i = 0;
            while i + 1 < nums.len() {
                if nums[i + 1] - nums[i] <= d {
                    cnt += 1;
                    i += 2;
                } else {
                    i += 1;
                }
            }
            cnt >= p
        };
        let mut lo = 0;
        let mut hi = nums[nums.len() - 1] - nums[0];
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}

fn main() {}
