struct Solution;
// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut st: Vec<usize> = Vec::new();
        for i in 0..n {
            while !st.is_empty() && nums[*st.last().unwrap()] < nums[i] {
                st.pop();
            }
            left[i] = if st.is_empty() { -1 } else { *st.last().unwrap() as i32 };
            st.push(i);
        }
        st.clear();
        for i in (0..n).rev() {
            while !st.is_empty() && nums[*st.last().unwrap()] <= nums[i] {
                st.pop();
            }
            right[i] = if st.is_empty() { n as i32 } else { *st.last().unwrap() as i32 };
            st.push(i);
        }
        (0..n).map(|i| right[i] - left[i] - 1).collect()
    }
}

fn main() {}
