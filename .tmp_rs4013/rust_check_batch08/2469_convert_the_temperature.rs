struct Solution;
// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        vec![celsius + 273.15, celsius * 1.80 + 32.00]
    }
}

fn main() {}
