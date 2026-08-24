struct Solution;
// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0i32;
        let mut st: Vec<usize> = Vec::new();
        for i in (0..n).rev() {
            if st.is_empty() || nums[i] > nums[*st.last().unwrap()] {
                st.push(i);
            }
        }
        for i in 0..n {
            while !st.is_empty() && nums[i] > nums[*st.last().unwrap()] {
                let j = st.pop().unwrap();
                ans = ans.max((j - i + 1) as i32);
            }
        }
        ans
    }
}

fn main() {}
