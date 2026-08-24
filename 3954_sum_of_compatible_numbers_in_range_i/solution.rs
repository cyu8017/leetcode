// LeetCode 3954 - Sum Of Compatible Numbers In Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

impl Solution {
    pub fn sum_of_good_integers(n: i32, k: i32) -> i32 {
        let start = 1.max(n - k);
        let end = n + k;
        let mut ans = 0;
        for x in start..=end {
            if (n & x) == 0 {
                ans += x;
            }
        }
        ans
    }
}
