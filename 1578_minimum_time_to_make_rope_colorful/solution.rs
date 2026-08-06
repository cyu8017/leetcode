// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let colors = colors.as_bytes();
        let mut answer = 0;
        let mut maximum = 0;
        for (i, &cost) in needed_time.iter().enumerate() {
            if i > 0 && colors[i] != colors[i - 1] {
                maximum = 0;
            }
            answer += maximum.min(cost);
            maximum = maximum.max(cost);
        }
        answer
    }
}
