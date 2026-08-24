struct Solution;
// LeetCode 3899 - Angles of a Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

impl Solution {
    pub fn internal_angles(mut sides: Vec<i32>) -> Vec<f64> {
        sides.sort_unstable();
        let a = sides[0] as f64;
        let b = sides[1] as f64;
        let c = sides[2] as f64;
        if a + b <= c {
            return vec![];
        }
        let pi = std::f64::consts::PI;
        let aa = ((b * b + c * c - a * a) / (2.0 * b * c)).acos() * 180.0 / pi;
        let bb = ((a * a + c * c - b * b) / (2.0 * a * c)).acos() * 180.0 / pi;
        let cc = 180.0 - aa - bb;
        vec![aa, bb, cc]
    }
}
