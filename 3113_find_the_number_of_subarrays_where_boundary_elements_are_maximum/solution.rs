// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>) -> i64 {
        let mut stk: Vec<(i32, i64)> = Vec::new();
        let mut ans = 0i64;
        for x in nums {
            while !stk.is_empty() && stk.last().unwrap().0 < x {
                stk.pop();
            }
            if stk.is_empty() || stk.last().unwrap().0 > x {
                stk.push((x, 1));
            } else {
                stk.last_mut().unwrap().1 += 1;
            }
            ans += stk.last().unwrap().1;
        }
        ans
    }
}
