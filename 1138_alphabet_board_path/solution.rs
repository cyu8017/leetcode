// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

impl Solution {
    pub fn alphabet_board_path(target: String) -> String {
        let mut r = 0i32;
        let mut c = 0i32;
        let mut out = String::new();
        for ch in target.bytes() {
            let tr = ((ch - b'a') / 5) as i32;
            let tc = ((ch - b'a') % 5) as i32;
            while r > tr {
                out.push('U');
                r -= 1;
            }
            while c > tc {
                out.push('L');
                c -= 1;
            }
            while c < tc {
                out.push('R');
                c += 1;
            }
            while r < tr {
                out.push('D');
                r += 1;
            }
            out.push('!');
        }
        out
    }
}
