// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut ans = 0i64;
        let mut imin = -1i32;
        let mut imax = -1i32;
        let mut ibad = -1i32;
        for (i, &x) in nums.iter().enumerate() {
            let i = i as i32;
            if x < min_k || x > max_k {
                ibad = i;
            }
            if x == min_k {
                imin = i;
            }
            if x == max_k {
                imax = i;
            }
            let bound = imin.min(imax);
            if bound > ibad {
                ans += (bound - ibad) as i64;
            }
        }
        ans
    }
}
