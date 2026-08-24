// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

impl Solution {
    pub fn split_array(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut s = vec![0i64; n];
        let mut f = vec![true; n];
        let mut g = vec![true; n];
        s[0] = nums[0] as i64;
        for i in 1..n {
            s[i] = s[i - 1] + nums[i] as i64;
            f[i] = f[i - 1];
            if nums[i] <= nums[i - 1] {
                f[i] = false;
            }
        }
        for i in (0..n - 1).rev() {
            g[i] = g[i + 1];
            if nums[i] <= nums[i + 1] {
                g[i] = false;
            }
        }
        let inf = i64::MAX / 4;
        let mut ans = inf;
        for i in 0..n - 1 {
            if f[i] && g[i + 1] {
                let s1 = s[i];
                let s2 = s[n - 1] - s[i];
                ans = ans.min((s1 - s2).abs());
            }
        }
        if ans < inf {
            ans
        } else {
            -1
        }
    }
}
