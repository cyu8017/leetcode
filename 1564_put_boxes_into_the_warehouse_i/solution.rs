// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

impl Solution {
    pub fn max_boxes_in_warehouse(mut boxes: Vec<i32>, mut warehouse: Vec<i32>) -> i32 {
        for i in 1..warehouse.len() {
            warehouse[i] = warehouse[i].min(warehouse[i - 1]);
        }
        boxes.sort_unstable();
        let mut room = warehouse.len() as i32 - 1;
        let mut used = 0;
        for box_h in boxes {
            while room >= 0 && warehouse[room as usize] < box_h {
                room -= 1;
            }
            if room < 0 {
                break;
            }
            used += 1;
            room -= 1;
        }
        used
    }
}
