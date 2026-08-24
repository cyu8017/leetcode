// LeetCode 2383 - Minimum Hours of Training to Win a Competition
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

impl Solution {
    pub fn min_number_of_hours(
        initial_energy: i32,
        initial_experience: i32,
        energy: Vec<i32>,
        experience: Vec<i32>,
    ) -> i32 {
        let mut ans = 0;
        let mut en = initial_energy;
        let mut ex = initial_experience;
        for i in 0..energy.len() {
            if en <= energy[i] {
                let need = energy[i] - en + 1;
                ans += need;
                en += need;
            }
            if ex <= experience[i] {
                let need = experience[i] - ex + 1;
                ans += need;
                ex += need;
            }
            en -= energy[i];
            ex += experience[i];
        }
        ans
    }
}
