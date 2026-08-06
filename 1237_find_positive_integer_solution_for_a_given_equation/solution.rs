// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

trait CustomFunction {
    fn f(&self, x: i32, y: i32) -> i32;
}

impl Solution {
    pub fn find_solution(customfunction: &impl CustomFunction, z: i32) -> Vec<Vec<i32>> {
        let mut ans = Vec::new();
        let mut x = 1;
        let mut y = 1000;
        while x <= 1000 && y >= 1 {
            let value = customfunction.f(x, y);
            if value == z {
                ans.push(vec![x, y]);
                x += 1;
                y -= 1;
            } else if value < z {
                x += 1;
            } else {
                y -= 1;
            }
        }
        ans
    }
}
