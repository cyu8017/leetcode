// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

impl Solution {
    pub fn next_beautiful_number(n: i32) -> i32 {
        fn balanced(mut x: i32) -> bool {
            let mut cnt = [0; 10];
            while x > 0 {
                cnt[(x % 10) as usize] += 1;
                x /= 10;
            }
            for d in 0..10 {
                if cnt[d] != 0 && cnt[d] != d {
                    return false;
                }
            }
            true
        }
        let mut x = n + 1;
        loop {
            if balanced(x) {
                return x;
            }
            x += 1;
        }
    }
}
