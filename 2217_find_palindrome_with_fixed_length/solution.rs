// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

impl Solution {
    pub fn kth_palindrome(queries: Vec<i32>, int_length: i32) -> Vec<i64> {
        let half = (int_length + 1) / 2;
        let mut start = 1i32;
        for _ in 1..half {
            start *= 10;
        }
        let total = start * 9;
        let mut ans = vec![0i64; queries.len()];
        for (i, &q) in queries.iter().enumerate() {
            if q > total {
                ans[i] = -1;
                continue;
            }
            let left = start + q - 1;
            let mut pal = left as i64;
            let mut x = left;
            if int_length % 2 == 1 {
                x /= 10;
            }
            while x > 0 {
                pal = pal * 10 + (x % 10) as i64;
                x /= 10;
            }
            ans[i] = pal;
        }
        ans
    }
}
