struct Solution;
// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

impl Solution {
    pub fn optimal_division(nums: Vec<i32>) -> String {
        if nums.len() == 1 {
            return nums[0].to_string();
        }
        if nums.len() == 2 {
            return format!("{}/{}", nums[0], nums[1]);
        }
        let mut result = format!("{}/(", nums[0]);
        for (i, num) in nums.iter().enumerate().skip(1) {
            if i > 1 {
                result.push('/');
            }
            result.push_str(&num.to_string());
        }
        result.push(')');
        result
    }
}

fn main() {}
