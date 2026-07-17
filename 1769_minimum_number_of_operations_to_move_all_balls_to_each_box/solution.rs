// LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box
// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

impl Solution {
    pub fn min_operations(boxes: String) -> Vec<i32> {
        let bytes = boxes.as_bytes();
        let n = bytes.len();
        let mut ans = vec![0i32; n];
        let mut balls = 0i32;
        let mut ops = 0i32;
        for i in 1..n {
            balls += (bytes[i - 1] - b'0') as i32;
            ops += balls;
            ans[i] = ops;
        }
        balls = 0;
        ops = 0;
        for i in (0..n.saturating_sub(1)).rev() {
            balls += (bytes[i + 1] - b'0') as i32;
            ops += balls;
            ans[i] += ops;
        }
        ans
    }
}
