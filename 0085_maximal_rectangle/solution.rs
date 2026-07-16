// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() {
            return 0;
        }

        let cols = matrix[0].len();
        let mut heights = vec![0; cols];
        let mut max_area = 0;

        for row in &matrix {
            for j in 0..cols {
                heights[j] = if row[j] == '1' { heights[j] + 1 } else { 0 };
            }
            max_area = max_area.max(Self::largest_histogram(&heights));
        }

        max_area
    }

    fn largest_histogram(heights: &[i32]) -> i32 {
        let mut stack: Vec<usize> = Vec::new();
        let mut max_area = 0;
        let mut extended = heights.to_vec();
        extended.push(0);

        for i in 0..extended.len() {
            let height = extended[i];
            while let Some(&top) = stack.last() {
                if extended[top] <= height {
                    break;
                }
                let h = extended[stack.pop().unwrap()];
                let width = if stack.is_empty() {
                    i as i32
                } else {
                    (i - stack.last().unwrap() - 1) as i32
                };
                max_area = max_area.max(h * width);
            }
            stack.push(i);
        }

        max_area
    }
}
