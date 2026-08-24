// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

impl Solution {
    pub fn sum_subarray_mins(arr: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = arr.len();
        let mut left = vec![-1i32; n];
        let mut right = vec![n as i32; n];
        let mut st = Vec::new();
        for i in 0..n {
            while st.last().map_or(false, |&j: &usize| arr[j] > arr[i]) {
                st.pop();
            }
            left[i] = st.last().map_or(-1, |&j| j as i32);
            st.push(i);
        }
        st.clear();
        for i in (0..n).rev() {
            while st.last().map_or(false, |&j: &usize| arr[j] >= arr[i]) {
                st.pop();
            }
            right[i] = st.last().map_or(n as i32, |&j| j as i32);
            st.push(i);
        }
        let mut ans = 0i64;
        for i in 0..n {
            ans = (ans + arr[i] as i64 * (i as i32 - left[i]) as i64 * (right[i] - i as i32) as i64)
                % MOD;
        }
        ans as i32
    }
}
