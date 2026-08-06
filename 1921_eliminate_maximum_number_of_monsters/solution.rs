// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

impl Solution {
    pub fn eliminate_maximum(dist: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut arrival: Vec<i32> = dist
            .iter()
            .zip(speed.iter())
            .map(|(&d, &s)| (d + s - 1) / s)
            .collect();
        arrival.sort_unstable();
        for (i, &t) in arrival.iter().enumerate() {
            if t <= i as i32 {
                return i as i32;
            }
        }
        arrival.len() as i32
    }
}
