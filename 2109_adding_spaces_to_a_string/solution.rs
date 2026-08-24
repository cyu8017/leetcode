// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

impl Solution {
    pub fn add_spaces(s: String, spaces: Vec<i32>) -> String {
        let mut b = String::with_capacity(s.len() + spaces.len());
        let mut j = 0;
        for (i, ch) in s.chars().enumerate() {
            if j < spaces.len() && spaces[j] as usize == i {
                b.push(' ');
                j += 1;
            }
            b.push(ch);
        }
        b
    }
}
