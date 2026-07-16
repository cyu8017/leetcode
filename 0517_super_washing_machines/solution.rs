// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

impl Solution {
    pub fn find_min_moves(machines: Vec<i32>) -> i32 {
        let total: i64 = machines.iter().map(|&value| value as i64).sum();
        let count = machines.len() as i64;
        if total % count != 0 {
            return -1;
        }
        let target = (total / count) as i32;
        let mut prefix = 0i64;
        let mut result = 0;
        for clothes in machines {
            let diff = clothes - target;
            prefix += diff as i64;
            result = result.max(prefix.abs() as i32).max(diff.abs());
        }
        result
    }
}
