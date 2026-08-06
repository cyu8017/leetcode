// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

impl Solution {
    pub fn max_length(arr: Vec<String>) -> i32 {
        let mut masks = vec![(0i32, 0i32)];
        for word in arr {
            let mut mask = 0i32;
            let mut ok = true;
            for b in word.bytes() {
                let bit = 1 << (b - b'a');
                if mask & bit != 0 {
                    ok = false;
                    break;
                }
                mask |= bit;
            }
            if !ok || mask.count_ones() as usize != word.len() {
                continue;
            }
            let cur = masks.clone();
            for (used, length) in cur {
                if used & mask == 0 {
                    masks.push((used | mask, length + word.len() as i32));
                }
            }
        }
        masks.into_iter().map(|(_, l)| l).max().unwrap_or(0)
    }
}
