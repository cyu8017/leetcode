// LeetCode 1499 - Max Value of Equation
// https://leetcode.com/problems/max-value-of-equation/

use std::collections::VecDeque;

impl Solution {
    pub fn find_max_value_of_equation(points: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut q: VecDeque<(i32, i32)> = VecDeque::new();
        let mut ans = i32::MIN;
        for p in points {
            let (x, y) = (p[0], p[1]);
            while q.front().map(|&(qx, _)| x - qx > k).unwrap_or(false) {
                q.pop_front();
            }
            if let Some(&(_, qv)) = q.front() {
                ans = ans.max(x + y + qv);
            }
            let value = y - x;
            while q.back().map(|&(_, bv)| bv <= value).unwrap_or(false) {
                q.pop_back();
            }
            q.push_back((x, value));
        }
        ans
    }
}
