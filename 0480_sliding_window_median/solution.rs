// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

impl Solution {
    pub fn median_sliding_window(nums: Vec<i32>, k: i32) -> Vec<f64> {
        let k = k as usize;
        let mut window = nums[..k].to_vec();
        window.sort_unstable();
        let mut result = Vec::with_capacity(nums.len() - k + 1);

        let mut append_median = |window: &Vec<i32>, result: &mut Vec<f64>| {
            if k % 2 == 1 {
                result.push(window[k / 2] as f64);
            } else {
                result.push((window[k / 2 - 1] as f64 + window[k / 2] as f64) / 2.0);
            }
        };

        append_median(&window, &mut result);
        for index in k..nums.len() {
            let outgoing = nums[index - k];
            let incoming = nums[index];
            if let Ok(remove_index) = window.binary_search(&outgoing) {
                window.remove(remove_index);
            }
            let insert_index = window.partition_point(|value| *value < incoming);
            window.insert(insert_index, incoming);
            append_median(&window, &mut result);
        }
        result
    }
}
