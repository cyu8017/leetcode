// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

impl Solution {
    pub fn minimum_boxes(n: i32) -> i32 {
        let n = n as i64;
        let mut height: i64 = 0;
        let mut used: i64 = 0;
        let mut base: i64 = 0;
        while used + (height + 1) * (height + 2) / 2 <= n {
            height += 1;
            let layer = height * (height + 1) / 2;
            used += layer;
            base += height;
        }
        let mut extra: i64 = 0;
        while used < n {
            extra += 1;
            used += extra;
        }
        (base + extra) as i32
    }
}
