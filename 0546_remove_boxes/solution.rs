// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

use std::cmp::max;

impl Solution {
    pub fn remove_boxes(boxes: Vec<i32>) -> i32 {
        let n = boxes.len();
        let mut memo = vec![vec![vec![-1; n + 1]; n]; n];

        fn dp(
            left: usize,
            mut right: usize,
            mut streak: usize,
            boxes: &[i32],
            memo: &mut Vec<Vec<Vec<i32>>>,
        ) -> i32 {
            if left > right {
                return 0;
            }
            if memo[left][right][streak] >= 0 {
                return memo[left][right][streak];
            }

            while right > left && boxes[right] == boxes[right - 1] {
                right -= 1;
                streak += 1;
            }

            let mut best =
                ((streak + 1) * (streak + 1)) as i32 + dp(left, right - 1, 0, boxes, memo);
            for index in left..right {
                if boxes[index] == boxes[right] {
                    best = max(
                        best,
                        dp(left, index, streak + 1, boxes, memo)
                            + dp(index + 1, right - 1, 0, boxes, memo),
                    );
                }
            }

            memo[left][right][streak] = best;
            best
        }

        dp(0, n - 1, 0, &boxes, &mut memo)
    }
}
