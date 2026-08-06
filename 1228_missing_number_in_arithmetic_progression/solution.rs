// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

impl Solution {
    pub fn missing_number(arr: Vec<i32>) -> i32 {
        let difference = (arr[arr.len() - 1] - arr[0]) / arr.len() as i32;
        for i in 1..arr.len() {
            let expected = arr[0] + i as i32 * difference;
            if arr[i] != expected {
                return expected;
            }
        }
        arr[0]
    }
}
