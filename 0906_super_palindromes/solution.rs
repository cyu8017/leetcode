// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

impl Solution {
    pub fn superpalindromes_in_range(left: String, right: String) -> i32 {
        let l: i64 = left.parse().unwrap();
        let r: i64 = right.parse().unwrap();
        fn is_pal(x: i64) -> bool {
            let s = x.to_string();
            s.bytes().eq(s.bytes().rev())
        }
        let mut ans = 0;
        for k in 1..=100000i64 {
            let s = k.to_string();
            let rev: String = s.chars().rev().collect();
            let pal: i64 = format!("{}{}", s, rev).parse().unwrap();
            let sq = pal.saturating_mul(pal);
            if sq > r {
                break;
            }
            if sq >= l && is_pal(sq) {
                ans += 1;
            }
        }
        for k in 1..=100000i64 {
            let s = k.to_string();
            let rev: String = s.chars().take(s.len() - 1).collect::<String>().chars().rev().collect();
            let pal: i64 = format!("{}{}", s, rev).parse().unwrap();
            let sq = pal.saturating_mul(pal);
            if sq > r {
                break;
            }
            if sq >= l && is_pal(sq) {
                ans += 1;
            }
        }
        ans
    }
}
