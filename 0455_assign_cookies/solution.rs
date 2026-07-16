// LeetCode 0455 - Assign Cookies
// https://leetcode.com/problems/assign-cookies/

impl Solution {
    pub fn find_content_children(g: &mut Vec<i32>, s: &mut Vec<i32>) -> i32 {
        g.sort_unstable();
        s.sort_unstable();

        let mut child = 0usize;
        for cookie in s {
            if child < g.len() && *cookie >= g[child] {
                child += 1;
            }
        }
        child as i32
    }
}
