// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-string-shifts/

impl Solution {
    pub fn string_shift(s: String, shift: Vec<Vec<i32>>) -> String {
        let n = s.len() as i32;
        let mut offset = 0i32;
        for sh in shift {
            offset += if sh[0] == 1 { sh[1] } else { -sh[1] };
        }
        offset = ((offset % n) + n) % n;
        if offset == 0 {
            return s;
        }
        let offset = offset as usize;
        format!("{}{}", &s[s.len() - offset..], &s[..s.len() - offset])
    }
}
