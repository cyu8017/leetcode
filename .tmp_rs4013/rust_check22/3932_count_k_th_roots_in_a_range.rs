struct Solution;
// LeetCode 3932 - Count K Th Roots In A Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/

impl Solution {
    pub fn count_kth_roots(l: i32, r: i32, k: i32) -> i32 {
        if k == 1 {
            return r - l + 1;
        }
        let mut ans = 0;
        let mut x = 0i64;
        loop {
            let mut y = 1i64;
            let mut too_big = false;
            for _ in 0..k {
                if x != 0 && y > r as i64 / x {
                    too_big = true;
                    break;
                }
                y *= x;
                if y > r as i64 {
                    break;
                }
            }
            if too_big || y > r as i64 {
                break;
            }
            if l as i64 <= y && y <= r as i64 {
                ans += 1;
            }
            x += 1;
        }
        ans
    }
}

fn main() {}
