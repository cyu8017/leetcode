// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

impl Solution {
    pub fn falling_squares(positions: Vec<Vec<i32>>) -> Vec<i32> {
        let mut intervals: Vec<(i32, i32, i32)> = Vec::new();
        let mut answer = Vec::new();
        let mut max_height = 0;
        for pos in positions {
            let left = pos[0];
            let side = pos[1];
            let right = left + side;
            let mut base = 0;
            for &(l, r, height) in &intervals {
                if r > left && l < right {
                    base = base.max(height);
                }
            }
            let height = base + side;
            intervals.push((left, right, height));
            max_height = max_height.max(height);
            answer.push(max_height);
        }
        answer
    }
}
