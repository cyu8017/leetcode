// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

impl Solution {
    pub fn get_collision_times(cars: Vec<Vec<i32>>) -> Vec<f64> {
        let n = cars.len();
        let mut ans = vec![-1.0f64; n];
        let mut stack: Vec<usize> = Vec::new();
        for i in (0..n).rev() {
            let pos = cars[i][0];
            let speed = cars[i][1];
            while let Some(&j) = stack.last() {
                if speed <= cars[j][1] {
                    stack.pop();
                    continue;
                }
                let t = (cars[j][0] - pos) as f64 / (speed - cars[j][1]) as f64;
                if ans[j] < 0.0 || t <= ans[j] {
                    ans[i] = t;
                    break;
                }
                stack.pop();
            }
            stack.push(i);
        }
        ans
    }
}
