// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let b = blocks.as_bytes();
        let k = k as usize;
        let mut white = b[..k].iter().filter(|&&c| c == b'W').count() as i32;
        let mut ans = white;
        for i in k..b.len() {
            if b[i] == b'W' {
                white += 1;
            }
            if b[i - k] == b'W' {
                white -= 1;
            }
            ans = ans.min(white);
        }
        ans
    }
}
