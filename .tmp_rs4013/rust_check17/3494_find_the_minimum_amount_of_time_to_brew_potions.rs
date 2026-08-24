struct Solution;
// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

impl Solution {
    pub fn min_time(skill: Vec<i32>, mana: Vec<i32>) -> i64 {
        let n = skill.len();
        let m = mana.len();
        let mut done = vec![0i64; n];
        for j in 0..m {
            let mut t = 0i64;
            for i in 0..n {
                if done[i] > t {
                    t = done[i];
                }
                t += skill[i] as i64 * mana[j] as i64;
                done[i] = t;
            }
            for i in (0..n - 1).rev() {
                done[i] = done[i + 1] - skill[i + 1] as i64 * mana[j] as i64;
            }
        }
        done[n - 1]
    }
}

fn main() {}
