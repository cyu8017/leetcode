// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

impl Solution {
    pub fn maximum_population(logs: Vec<Vec<i32>>) -> i32 {
        let mut diff = [0i32; 101];
        for log in &logs {
            diff[(log[0] - 1950) as usize] += 1;
            diff[(log[1] - 1950) as usize] -= 1;
        }
        let mut best_year = 1950;
        let mut best_population = 0;
        let mut population = 0;
        for offset in 0..101 {
            population += diff[offset];
            if population > best_population {
                best_population = population;
                best_year = 1950 + offset as i32;
            }
        }
        best_year
    }
}
