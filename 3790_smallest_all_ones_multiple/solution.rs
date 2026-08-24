// LeetCode 3790 - Smallest All Ones Multiple
// https://leetcode.com/problems/smallest-all-ones-multiple/

impl Solution {
    pub fn min_all_one_multiple(k: i32) -> i32 {
        if (k & 1) == 0 {
            return -1;
        }
        let mut x = 1 % k;
        let mut ans = 1;
        for _ in 0..k {
            x = (x * 10 + 1) % k;
            ans += 1;
            if x == 0 {
                return ans;
            }
        }
        -1
    }
}
