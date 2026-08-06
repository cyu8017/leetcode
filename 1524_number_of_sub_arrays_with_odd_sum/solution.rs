// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        let mut counts = [1i64, 0];
        let mut parity = 0;
        let mut answer = 0i64;
        for value in arr {
            parity ^= value & 1;
            answer += counts[(parity ^ 1) as usize];
            counts[parity as usize] += 1;
        }
        (answer % 1_000_000_007) as i32
    }
}
