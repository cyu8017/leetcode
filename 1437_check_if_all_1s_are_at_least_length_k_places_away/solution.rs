// LeetCode 1437 - Check If All 1's Are at Least Length K Places Away
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut previous = -k - 1;
        for (i, &value) in nums.iter().enumerate() {
            if value == 1 {
                if i as i32 - previous <= k {
                    return false;
                }
                previous = i as i32;
            }
        }
        true
    }
}
