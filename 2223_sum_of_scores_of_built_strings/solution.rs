// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

impl Solution {
    pub fn sum_scores(s: String) -> i64 {
        let s = s.as_bytes();
        let n = s.len();
        let mut z = vec![0; n];
        let mut l = 0;
        let mut r = 0;
        for i in 1..n {
            if i <= r {
                z[i] = z[i - l].min(r - i + 1);
            }
            while i + z[i] < n && s[z[i]] == s[i + z[i]] {
                z[i] += 1;
            }
            if i + z[i] - 1 > r {
                l = i;
                r = i + z[i] - 1;
            }
        }
        let mut ans = n as i64;
        for i in 1..n {
            ans += z[i] as i64;
        }
        ans
    }
}
