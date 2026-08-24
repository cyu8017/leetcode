// LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

impl Solution {
    pub fn winner_of_game(colors: String) -> bool {
        let b = colors.as_bytes();
        let mut a = 0;
        let mut bb = 0;
        for i in 1..b.len().saturating_sub(1) {
            if b[i - 1] == b[i] && b[i] == b[i + 1] {
                if b[i] == b'A' {
                    a += 1;
                } else {
                    bb += 1;
                }
            }
        }
        a > bb
    }
}
