// LeetCode 1944 - Number of Visible People in a Queue
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

impl Solution {
    pub fn can_see_persons_count(heights: Vec<i32>) -> Vec<i32> {
        let n = heights.len();
        let mut ans = vec![0; n];
        let mut stack: Vec<i32> = Vec::new();
        for i in (0..n).rev() {
            let mut count = 0;
            while let Some(&top) = stack.last() {
                if heights[i] > top {
                    stack.pop();
                    count += 1;
                } else {
                    break;
                }
            }
            if !stack.is_empty() {
                count += 1;
            }
            ans[i] = count;
            stack.push(heights[i]);
        }
        ans
    }
}
