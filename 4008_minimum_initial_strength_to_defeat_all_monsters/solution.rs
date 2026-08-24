// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

impl Solution {
    pub fn min_initial_strength(monsters: Vec<i32>, boosts: Vec<Vec<i32>>) -> i64 {
        let n = monsters.len();
        let mut d = vec![0i64; n + 1];
        for b in &boosts {
            d[b[0] as usize] += b[2] as i64;
            d[b[1] as usize + 1] -= b[2] as i64;
        }
        let check = |mut v: i64| -> bool {
            let mut bonus = 0i64;
            for i in 0..n {
                bonus += d[i];
                if v + bonus < monsters[i] as i64 {
                    return false;
                }
                v -= monsters[i] as i64;
                if v < 0 {
                    v = 0;
                }
            }
            true
        };
        let mut left = 0i64;
        let mut right = 1_000_000_000_000_000i64;
        while left < right {
            let mid = (left + right) / 2;
            if check(mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}
