struct Solution;
// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

impl Solution {
    pub fn maximum_points(mut enemy_energies: Vec<i32>, mut current_energy: i32) -> i64 {
        enemy_energies.sort_unstable();
        if current_energy < enemy_energies[0] {
            return 0;
        }
        let mut ans = 0i64;
        for i in (0..enemy_energies.len()).rev() {
            ans += (current_energy / enemy_energies[0]) as i64;
            current_energy %= enemy_energies[0];
            current_energy += enemy_energies[i];
        }
        ans
    }
}

fn main() {}
