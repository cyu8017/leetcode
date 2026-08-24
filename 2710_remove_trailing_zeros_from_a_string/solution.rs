// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

impl Solution {
    pub fn remove_trailing_zeros(mut num: String) -> String {
        while num.ends_with('0') {
            num.pop();
        }
        num
    }
}
