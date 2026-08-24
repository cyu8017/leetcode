// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

impl Solution {
    fn is_palindrome(s: &[u8]) -> bool {
        let m = s.len();
        for i in 0..m / 2 {
            if s[i] != s[m - 1 - i] {
                return false;
            }
        }
        true
    }

    fn get_pals() -> Vec<i32> {
        let n = 1 << 14;
        let mut pals = Vec::new();
        for i in 0..n {
            let mut x = i;
            let mut s = Vec::new();
            if x == 0 {
                s.push(b'0');
            } else {
                while x > 0 {
                    s.push(b'0' + (x & 1) as u8);
                    x >>= 1;
                }
                s.reverse();
            }
            if Self::is_palindrome(&s) {
                pals.push(i);
            }
        }
        pals
    }

    pub fn min_operations(nums: Vec<i32>) -> Vec<i32> {
        let p = Self::get_pals();
        let mut ans = vec![0; nums.len()];
        for (k, &x) in nums.iter().enumerate() {
            let it = p.partition_point(|&v| v < x);
            let mut t = i32::MAX;
            if it < p.len() {
                t = p[it] - x;
            }
            if it > 0 {
                t = t.min(x - p[it - 1]);
            }
            ans[k] = t;
        }
        ans
    }
}
