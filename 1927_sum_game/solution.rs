// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

impl Solution {
    pub fn sum_game(num: String) -> bool {
        let n = num.len();
        let half = n / 2;
        let score = |s: &str| -> i32 {
            let mut q = 0;
            let mut dig = 0;
            for c in s.chars() {
                if c == '?' {
                    q += 1;
                } else {
                    dig += c.to_digit(10).unwrap() as i32;
                }
            }
            dig * 2 + q * 9
        };
        score(&num[..half]) != score(&num[half..])
    }
}
