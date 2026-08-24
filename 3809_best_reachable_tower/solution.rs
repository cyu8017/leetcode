// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

impl Solution {
    pub fn best_tower(towers: Vec<Vec<i32>>, center: Vec<i32>, radius: i32) -> Vec<i32> {
        let cx = center[0];
        let cy = center[1];
        let mut idx = -1i32;
        for i in 0..towers.len() {
            let x = towers[i][0];
            let y = towers[i][1];
            let q = towers[i][2];
            let dist = (x - cx).abs() + (y - cy).abs();
            if dist > radius {
                continue;
            }
            if idx == -1
                || towers[idx as usize][2] < q
                || (towers[idx as usize][2] == q
                    && (x < towers[idx as usize][0]
                        || (x == towers[idx as usize][0] && y < towers[idx as usize][1])))
            {
                idx = i as i32;
            }
        }
        if idx == -1 {
            vec![-1, -1]
        } else {
            vec![towers[idx as usize][0], towers[idx as usize][1]]
        }
    }
}
