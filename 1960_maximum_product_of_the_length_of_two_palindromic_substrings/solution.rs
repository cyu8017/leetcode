// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

impl Solution {
    pub fn max_product(s: String) -> i64 {
        let s: Vec<u8> = s.into_bytes();
        let n = s.len();
        let mut radius = vec![0usize; n];
        let mut center = 0usize;
        let mut right = 0usize;
        for i in 0..n {
            if i < right {
                radius[i] = (right - i).min(radius[2 * center - i]);
            }
            while i >= radius[i] + 1
                && i + radius[i] + 1 < n
                && s[i - radius[i] - 1] == s[i + radius[i] + 1]
            {
                radius[i] += 1;
            }
            if i + radius[i] > right {
                center = i;
                right = i + radius[i];
            }
        }

        let mut end = vec![1i64; n];
        let mut start = vec![1i64; n];
        for i in 0..n {
            let r = radius[i];
            end[i + r] = end[i + r].max(2 * r as i64 + 1);
            start[i - r] = start[i - r].max(2 * r as i64 + 1);
        }
        for i in (0..n - 1).rev() {
            end[i] = end[i].max(end[i + 1] - 2);
        }
        for i in 1..n {
            start[i] = start[i].max(start[i - 1] - 2);
        }

        let mut pre = vec![0i64; n];
        pre[0] = end[0];
        for i in 1..n {
            pre[i] = pre[i - 1].max(end[i]);
        }
        let mut suf = vec![0i64; n];
        suf[n - 1] = start[n - 1];
        for i in (0..n - 1).rev() {
            suf[i] = suf[i + 1].max(start[i]);
        }

        (0..n - 1).map(|i| pre[i] * suf[i + 1]).max().unwrap()
    }
}
