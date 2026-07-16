// LeetCode 0316 - Remove Duplicate Letters
// https://leetcode.com/problems/remove-duplicate-letters/

impl Solution {
    pub fn remove_duplicate_letters(s: String) -> String {
        let bytes = s.as_bytes();
        let mut last_index = [usize::MAX; 256];
        for (index, &character) in bytes.iter().enumerate() {
            last_index[character as usize] = index;
        }

        let mut stack: Vec<u8> = Vec::new();
        let mut seen = [false; 256];
        for (index, &character) in bytes.iter().enumerate() {
            if seen[character as usize] {
                continue;
            }
            while let Some(&top) = stack.last() {
                if top > character && last_index[top as usize] > index {
                    seen[top as usize] = false;
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(character);
            seen[character as usize] = true;
        }

        String::from_utf8(stack).unwrap_or_default()
    }
}
