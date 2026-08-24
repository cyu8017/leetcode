// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

impl Solution {
    pub fn score(cards: Vec<String>, x: char) -> i32 {
        let mut xx = 0;
        let mut left = [0i32; 26];
        let mut right = [0i32; 26];
        for c in cards {
            let b = c.as_bytes();
            let a = b[0] as char;
            let d = b[1] as char;
            if a == x && d == x {
                xx += 1;
            } else if a == x {
                left[(d as u8 - b'a') as usize] += 1;
            } else if d == x {
                right[(a as u8 - b'a') as usize] += 1;
            }
        }
        let pair_group = |arr: &[i32; 26]| -> (i32, i32) {
            let mut total = 0;
            let mut mx = 0;
            for &v in arr {
                total += v;
                mx = mx.max(v);
            }
            let mut pairs = total / 2;
            if total - mx < pairs {
                pairs = total - mx;
            }
            (pairs, total - 2 * pairs)
        };
        let (lp, lr) = pair_group(&left);
        let (rp, rr) = pair_group(&right);
        let mut ans = lp + rp;
        let rem = lr + rr;
        let use_xx = xx.min(rem);
        ans += use_xx;
        xx -= use_xx;
        ans += xx / 2;
        ans
    }
}
