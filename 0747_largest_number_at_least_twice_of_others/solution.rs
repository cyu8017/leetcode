// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

impl Solution {
    pub fn dominant_index(nums: Vec<i32>) -> i32 {
        let mut first = -1;
        let mut second = -1;
        let mut index = -1;
        for (i, &num) in nums.iter().enumerate() {
            if num > first {
                second = first;
                first = num;
                index = i as i32;
            } else if num > second {
                second = num;
            }
        }
        if first >= 2 * second {
            index
        } else {
            -1
        }
    }
}
