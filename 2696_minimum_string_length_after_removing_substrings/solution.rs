// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

impl Solution {
    pub fn min_length(s: String) -> i32 {
        let mut st = String::new();
        for c in s.chars() {
            if let Some(last) = st.chars().last() {
                if (last == 'A' && c == 'B') || (last == 'C' && c == 'D') {
                    st.pop();
                    continue;
                }
            }
            st.push(c);
        }
        st.len() as i32
    }
}
