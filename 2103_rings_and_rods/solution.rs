// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

impl Solution {
    pub fn count_points(rings: String) -> i32 {
        let mut mask = [0i32; 10];
        let b = rings.as_bytes();
        let mut i = 0;
        while i < b.len() {
            let c = b[i];
            let r = (b[i + 1] - b'0') as usize;
            let bit = if c == b'R' { 1 } else if c == b'G' { 2 } else { 4 };
            mask[r] |= bit;
            i += 2;
        }
        mask.iter().filter(|&&m| m == 7).count() as i32
    }
}
