// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

impl Solution {
    pub fn cyclic_generator(arr: Vec<i32>, start_index: i32) -> Box<dyn FnMut() -> i32> {
        let n = arr.len();
        let mut i = start_index as usize;
        Box::new(move || {
            let v = arr[i];
            i = (i + 1) % n;
            v
        })
    }
}
