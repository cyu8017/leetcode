// LeetCode 0370 - Range Addition
// https://leetcode.com/problems/range-addition/

impl Solution {
    pub fn get_modified_array(length: i32, updates: Vec<Vec<i32>>) -> Vec<i32> {
        let length = length as usize;
        let mut diff = vec![0; length + 1];

        for update in updates {
            let start = update[0] as usize;
            let end = update[1] as usize;
            let inc = update[2];
            diff[start] += inc;
            if end + 1 < diff.len() {
                diff[end + 1] -= inc;
            }
        }

        let mut result = vec![0; length];
        let mut running = 0;
        for index in 0..length {
            running += diff[index];
            result[index] = running;
        }

        result
    }
}
