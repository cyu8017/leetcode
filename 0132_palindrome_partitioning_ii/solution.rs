// LeetCode 0132 - Palindrome Partitioning II
impl Solution {
    pub fn min_cut(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut pal = vec![vec![false; n]; n];
        for i in (0..n).rev() {
            for j in i..n {
                pal[i][j] = bytes[i] == bytes[j] && (j - i < 2 || pal[i + 1][j - 1]);
            }
        }
        let mut cuts = vec![0_i32; n];
        for i in 0..n {
            cuts[i] = i as i32;
            for j in 0..=i {
                if pal[j][i] { cuts[i] = if j == 0 { 0 } else { cuts[i].min(cuts[j - 1] + 1) }; }
            }
        }
        cuts[n - 1]
    }
}