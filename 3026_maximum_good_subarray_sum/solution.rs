// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let mut p: HashMap<i32, i64> = HashMap::new();
        p.insert(nums[0], 0);
        let mut s = 0i64;
        let n = nums.len();
        let mut ans = i64::MIN;
        for i in 0..n {
            s += nums[i] as i64;
            if let Some(&v) = p.get(&(nums[i] - k)) {
                ans = ans.max(s - v);
            }
            if let Some(&v) = p.get(&(nums[i] + k)) {
                ans = ans.max(s - v);
            }
            if i + 1 == n {
                break;
            }
            let nxt = nums[i + 1];
            if !p.contains_key(&nxt) || s < p[&nxt] {
                p.insert(nxt, s);
            }
        }
        if ans == i64::MIN { 0 } else { ans }
    }
}
