// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

impl Solution {
    pub fn max_boxes_in_warehouse(mut boxes: Vec<i32>, warehouse: Vec<i32>) -> i32 {
        let n = warehouse.len();
        let mut left = warehouse.clone();
        let mut right = warehouse.clone();
        for i in 1..n {
            left[i] = left[i].min(left[i - 1]);
        }
        for i in (0..n - 1).rev() {
            right[i] = right[i].min(right[i + 1]);
        }
        let mut capacity: Vec<i32> = (0..n).map(|i| left[i].max(right[i])).collect();
        capacity.sort_unstable();
        boxes.sort_unstable();
        let mut i = 0;
        for room in capacity {
            if i < boxes.len() && boxes[i] <= room {
                i += 1;
            }
        }
        i as i32
    }
}
