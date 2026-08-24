// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

impl Solution {
    pub fn maximum_even_split(mut final_sum: i64) -> Vec<i64> {
        if final_sum % 2 != 0 {
            return vec![];
        }
        let mut ans = Vec::new();
        let mut x = 2i64;
        while x <= final_sum {
            ans.push(x);
            final_sum -= x;
            x += 2;
        }
        if let Some(last) = ans.last_mut() {
            *last += final_sum;
        }
        ans
    }
}
