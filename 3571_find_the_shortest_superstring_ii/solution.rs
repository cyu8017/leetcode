// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

impl Solution {
    pub fn shortest_superstring(s1: String, s2: String) -> String {
        if s1.len() > s2.len() {
            return Self::shortest_superstring(s2, s1);
        }
        let m = s1.len();
        if s2.contains(&s1) {
            return s2;
        }
        for i in 0..m {
            if s2.starts_with(&s1[i..]) {
                return format!("{}{}", &s1[..i], s2);
            }
            let length = m - i;
            if s2.len() >= length && &s2[s2.len() - length..] == &s1[..length] {
                return format!("{}{}", s2, &s1[m - i..]);
            }
        }
        format!("{}{}", s1, s2)
    }
}
