// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

impl Solution {
    pub fn color_the_array(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut colors = vec![0; n];
        let mut ans = vec![0; queries.len()];
        let mut same = 0;
        for (i, q) in queries.iter().enumerate() {
            let idx = q[0] as usize;
            let color = q[1];
            if colors[idx] != 0 {
                if idx > 0 && colors[idx] == colors[idx - 1] {
                    same -= 1;
                }
                if idx + 1 < n && colors[idx] == colors[idx + 1] {
                    same -= 1;
                }
            }
            colors[idx] = color;
            if idx > 0 && colors[idx] == colors[idx - 1] {
                same += 1;
            }
            if idx + 1 < n && colors[idx] == colors[idx + 1] {
                same += 1;
            }
            ans[i] = same;
        }
        ans
    }
}
