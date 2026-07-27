// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

impl Solution {
    pub fn special_array(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        for x in 0..=n {
            let cnt = nums.iter().filter(|&&v| v >= x).count() as i32;
            if cnt == x {
                return x;
            }
        }
        -1
    }
}
