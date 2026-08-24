struct Solution;
// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

impl Solution {
    pub fn count_good_subarrays(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut l = vec![-1i32; n];
        let mut stk = Vec::new();
        for i in 0..n {
            let x = nums[i];
            while !stk.is_empty() {
                let last = *stk.last().unwrap();
                if nums[last] < x && (nums[last] | x) == x {
                    stk.pop();
                } else {
                    break;
                }
            }
            if !stk.is_empty() {
                l[i] = *stk.last().unwrap() as i32;
            }
            stk.push(i);
        }
        let mut r = vec![n as i32; n];
        stk.clear();
        for i in (0..n).rev() {
            while !stk.is_empty() {
                let last = *stk.last().unwrap();
                if (nums[last] | nums[i]) == nums[i] {
                    stk.pop();
                } else {
                    break;
                }
            }
            if !stk.is_empty() {
                r[i] = *stk.last().unwrap() as i32;
            }
            stk.push(i);
        }
        let mut ans = 0i64;
        for i in 0..n {
            ans += (i as i32 - l[i]) as i64 * (r[i] - i as i32) as i64;
        }
        ans
    }
}
