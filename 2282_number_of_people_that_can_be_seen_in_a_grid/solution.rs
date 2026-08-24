// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

impl Solution {
    pub fn see_people(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = heights.len();
        let n = heights[0].len();
        let mut ans = vec![vec![0; n]; m];
        for i in 0..m {
            let mut stack: Vec<usize> = Vec::new();
            for j in (0..n).rev() {
                let mut cnt = 0;
                while !stack.is_empty() && heights[i][*stack.last().unwrap()] < heights[i][j] {
                    stack.pop();
                    cnt += 1;
                }
                if !stack.is_empty() {
                    cnt += 1;
                }
                ans[i][j] += cnt;
                while !stack.is_empty() && heights[i][*stack.last().unwrap()] == heights[i][j] {
                    stack.pop();
                }
                stack.push(j);
            }
        }
        for j in 0..n {
            let mut stack: Vec<usize> = Vec::new();
            for i in (0..m).rev() {
                let mut cnt = 0;
                while !stack.is_empty() && heights[*stack.last().unwrap()][j] < heights[i][j] {
                    stack.pop();
                    cnt += 1;
                }
                if !stack.is_empty() {
                    cnt += 1;
                }
                ans[i][j] += cnt;
                while !stack.is_empty() && heights[*stack.last().unwrap()][j] == heights[i][j] {
                    stack.pop();
                }
                stack.push(i);
            }
        }
        ans
    }
}
