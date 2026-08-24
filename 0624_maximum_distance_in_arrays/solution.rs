// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

impl Solution {
    pub fn max_distance(arrays: Vec<Vec<i32>>) -> i32 {
        let mut min_val = arrays[0][0];
        let mut max_val = *arrays[0].last().unwrap();
        let mut best = 0;
        for arr in arrays.iter().skip(1) {
            let first = arr[0];
            let last = *arr.last().unwrap();
            best = best.max((last - min_val).abs()).max((max_val - first).abs());
            min_val = min_val.min(first);
            max_val = max_val.max(last);
        }
        best
    }
}
