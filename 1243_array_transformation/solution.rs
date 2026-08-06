// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

impl Solution {
    pub fn transform_array(mut arr: Vec<i32>) -> Vec<i32> {
        loop {
            let mut nxt = arr.clone();
            let mut changed = false;
            for i in 1..arr.len() - 1 {
                if arr[i] < arr[i - 1] && arr[i] < arr[i + 1] {
                    nxt[i] += 1;
                    changed = true;
                } else if arr[i] > arr[i - 1] && arr[i] > arr[i + 1] {
                    nxt[i] -= 1;
                    changed = true;
                }
            }
            if !changed {
                return arr;
            }
            arr = nxt;
        }
    }
}
