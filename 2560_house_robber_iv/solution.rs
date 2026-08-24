// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

impl Solution {
    pub fn min_capability(nums: Vec<i32>, k: i32) -> i32 {
        let mut lo = *nums.iter().min().unwrap();
        let mut hi = *nums.iter().max().unwrap();
        let ok = |cap: i32| {
            let mut cnt = 0;
            let mut i = 0;
            while i < nums.len() {
                if nums[i] <= cap {
                    cnt += 1;
                    i += 2;
                } else {
                    i += 1;
                }
            }
            cnt >= k
        };
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
