// LeetCode 3872 - Longest Arithmetic Sequence After Changing at Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

impl Solution {
    pub fn longest_arithmetic(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut d = vec![0; n];
        for i in 1..n {
            d[i] = nums[i] - nums[i - 1];
        }
        let mut f = vec![2; n];
        let mut g = vec![2; n];
        f[0] = 1;
        g[n - 1] = 1;
        for i in 2..n {
            if d[i] == d[i - 1] {
                f[i] = f[i - 1] + 1;
            }
        }
        for i in (0..n.saturating_sub(2)).rev() {
            if d[i + 1] == d[i + 2] {
                g[i] = g[i + 1] + 1;
            }
        }
        let mut ans = 3;
        for i in 0..n {
            ans = ans.max(f[i]).max(g[i]);
            if i > 0 {
                ans = ans.max(f[i - 1] + 1);
            }
            if i + 1 < n {
                ans = ans.max(g[i + 1] + 1);
            }
            if i > 0 && i < n - 1 {
                let mut diff = nums[i + 1] - nums[i - 1];
                if diff % 2 == 0 {
                    diff /= 2;
                    let mut k = 3;
                    if i > 1 && diff == d[i - 1] {
                        k += f[i - 1] - 1;
                    }
                    if i < n - 2 && diff == d[i + 2] {
                        k += g[i + 1] - 1;
                    }
                    ans = ans.max(k);
                }
            }
        }
        ans
    }
}
