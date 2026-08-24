// LeetCode 0925 - Long Pressed Name
// https://leetcode.com/problems/long-pressed-name/

impl Solution {
    pub fn is_long_pressed_name(name: String, typed: String) -> bool {
        let name: Vec<u8> = name.into_bytes();
        let typed: Vec<u8> = typed.into_bytes();
        let mut i = 0;
        let mut j = 0;
        while j < typed.len() {
            if i < name.len() && name[i] == typed[j] {
                i += 1;
                j += 1;
            } else if j > 0 && typed[j] == typed[j - 1] {
                j += 1;
            } else {
                return false;
            }
        }
        i == name.len()
    }
}
