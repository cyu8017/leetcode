// LeetCode 0383 - Ransom Note
// https://leetcode.com/problems/ransom-note/

impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut counts = [0i32; 26];

        for ch in magazine.bytes() {
            counts[(ch - b'a') as usize] += 1;
        }

        for ch in ransom_note.bytes() {
            let index = (ch - b'a') as usize;
            if counts[index] == 0 {
                return false;
            }
            counts[index] -= 1;
        }

        true
    }
}
