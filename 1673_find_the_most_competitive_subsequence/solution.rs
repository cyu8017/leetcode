// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

impl Solution {
    pub fn most_competitive(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let n = nums.len();
        let mut st = Vec::new();
        for (i, &x) in nums.iter().enumerate() {
            while !st.is_empty()
                && *st.last().unwrap() > x
                && st.len() - 1 + n - i >= k
            {
                st.pop();
            }
            if st.len() < k {
                st.push(x);
            }
        }
        st
    }
}
