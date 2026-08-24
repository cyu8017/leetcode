// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

impl Solution {
    pub fn second_greater_element(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![-1; n];
        let mut stack1 = Vec::new();
        let mut stack2 = Vec::new();
        for i in 0..n {
            let x = nums[i];
            while !stack2.is_empty() && nums[*stack2.last().unwrap()] < x {
                ans[stack2.pop().unwrap()] = x;
            }
            let mut tmp = Vec::new();
            while !stack1.is_empty() && nums[*stack1.last().unwrap()] < x {
                tmp.push(stack1.pop().unwrap());
            }
            for &j in tmp.iter().rev() {
                stack2.push(j);
            }
            stack1.push(i);
        }
        ans
    }
}
