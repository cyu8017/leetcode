struct Solution;
// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

impl Solution {
    pub fn min_damage(power: i32, damage: Vec<i32>, health: Vec<i32>) -> i64 {
        let n = damage.len();
        let mut arr = Vec::with_capacity(n);
        let mut total_dmg = 0i64;
        for i in 0..n {
            let hits = (health[i] + power - 1) / power;
            arr.push((damage[i], hits));
            total_dmg += damage[i] as i64;
        }
        arr.sort_by(|a, b| (a.1 as i64 * b.0 as i64).cmp(&(b.1 as i64 * a.0 as i64)));
        let mut ans = 0i64;
        let mut cur = total_dmg;
        for (dmg, hits) in arr {
            ans += cur * hits as i64;
            cur -= dmg as i64;
        }
        ans
    }
}

fn main() {}
