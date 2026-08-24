// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

impl Solution {
    pub fn minimum_buckets(hamsters: String) -> i32 {
        let mut b = hamsters.into_bytes();
        let mut ans = 0;
        let n = b.len();
        for i in 0..n {
            if b[i] != b'H' {
                continue;
            }
            if i > 0 && b[i - 1] == b'B' {
                continue;
            }
            if i + 1 < n && b[i + 1] == b'.' {
                b[i + 1] = b'B';
                ans += 1;
            } else if i > 0 && b[i - 1] == b'.' {
                b[i - 1] = b'B';
                ans += 1;
            } else {
                return -1;
            }
        }
        ans
    }
}
