// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

impl Solution {
    pub fn find_radius(houses: Vec<i32>, mut heaters: Vec<i32>) -> i32 {
        heaters.sort_unstable();
        let mut radius = 0;
        for house in houses {
            let position = heaters.partition_point(|value| *value < house);
            let mut best = i32::MAX;
            if position < heaters.len() {
                best = best.min((heaters[position] - house).abs());
            }
            if position > 0 {
                best = best.min((heaters[position - 1] - house).abs());
            }
            radius = radius.max(best);
        }
        radius
    }
}
