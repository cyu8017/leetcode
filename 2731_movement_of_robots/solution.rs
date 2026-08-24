// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

impl Solution {
    pub fn sum_distance(nums: Vec<i32>, s: String, d: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let mut pos: Vec<i64> = nums
            .iter()
            .enumerate()
            .map(|(i, &x)| x as i64 + if bytes[i] == b'R' { d as i64 } else { -(d as i64) })
            .collect();
        pos.sort_unstable();
        let mut ans = 0i64;
        let mut pref = 0i64;
        for (i, &p) in pos.iter().enumerate() {
            ans = (ans + p * i as i64 - pref) % MOD;
            pref += p;
        }
        ((ans % MOD + MOD) % MOD) as i32
    }
}
