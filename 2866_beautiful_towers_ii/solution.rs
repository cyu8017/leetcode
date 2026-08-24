// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

impl Solution {
    pub fn maximum_sum_of_heights(max_heights: Vec<i32>) -> i64 {
        let n = max_heights.len();
        let mut left = vec![0i64; n];
        let mut st: Vec<i32> = vec![-1];
        let mut sum = 0i64;
        for i in 0..n {
            while st.len() > 1 && max_heights[*st.last().unwrap() as usize] >= max_heights[i] {
                let j = st.pop().unwrap();
                sum -= max_heights[j as usize] as i64 * (j - *st.last().unwrap()) as i64;
            }
            sum += max_heights[i] as i64 * (i as i32 - *st.last().unwrap()) as i64;
            left[i] = sum;
            st.push(i as i32);
        }
        let mut right = vec![0i64; n];
        st = vec![n as i32];
        sum = 0;
        for i in (0..n).rev() {
            while st.len() > 1 && max_heights[*st.last().unwrap() as usize] >= max_heights[i] {
                let j = st.pop().unwrap();
                sum -= max_heights[j as usize] as i64 * (*st.last().unwrap() - j) as i64;
            }
            sum += max_heights[i] as i64 * (*st.last().unwrap() - i as i32) as i64;
            right[i] = sum;
            st.push(i as i32);
        }
        let mut ans = 0i64;
        for i in 0..n {
            ans = ans.max(left[i] + right[i] - max_heights[i] as i64);
        }
        ans
    }
}
