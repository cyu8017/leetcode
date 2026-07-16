// LeetCode 0414 - Third Maximum Number
// https://leetcode.com/problems/third-maximum-number/

impl Solution {
    pub fn third_max(nums: Vec<i32>) -> i32 {
        let mut first: Option<i32> = None;
        let mut second: Option<i32> = None;
        let mut third: Option<i32> = None;

        for value in nums {
            if Some(value) == first || Some(value) == second || Some(value) == third {
                continue;
            }
            if first.is_none() || value > first.unwrap() {
                third = second;
                second = first;
                first = Some(value);
            } else if second.is_none() || value > second.unwrap() {
                third = second;
                second = Some(value);
            } else if third.is_none() || value > third.unwrap() {
                third = Some(value);
            }
        }

        third.unwrap_or_else(|| first.unwrap())
    }
}
