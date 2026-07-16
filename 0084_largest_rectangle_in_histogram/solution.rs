// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let mut stack: Vec<usize> = Vec::new();
        let mut max_area = 0;
        let mut extended = heights;
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
