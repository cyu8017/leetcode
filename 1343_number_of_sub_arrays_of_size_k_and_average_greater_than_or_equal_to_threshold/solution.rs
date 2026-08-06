// LeetCode 1343 - Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>, k: i32, threshold: i32) -> i32 {
        let k = k as usize;
        let mut window: i32 = arr[..k].iter().sum();
        let mut answer = i32::from(window >= k as i32 * threshold);
        for i in k..arr.len() {
            window += arr[i] - arr[i - k];
            answer += i32::from(window >= k as i32 * threshold);
        }
        answer
    }
}
