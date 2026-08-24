// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

fn bit_width(mut k: u32) -> i32 {
    let mut w = 0;
    while k != 0 {
        w += 1;
        k >>= 1;
    }
    w
}

impl Solution {
    pub fn create_grid(k: i32) -> Vec<String> {
        if k <= 0 {
            return vec![];
        }
        let l = bit_width(k as u32);
        let m = 2 * l;
        let n = l + 3;
        let mut result = vec![vec![b'#'; n as usize]; m as usize];
        for i in 0..l {
            let r = 2 * i;
            result[r as usize][i as usize] = b'.';
            result[r as usize][(i + 1) as usize] = b'.';
            result[(r + 1) as usize][i as usize] = b'.';
            result[(r + 1) as usize][(i + 1) as usize] = b'.';
            if k & (1 << i) != 0 {
                for c in (i + 2)..n {
                    result[r as usize][c as usize] = b'.';
                }
            }
        }
        for r in 0..m {
            result[r as usize][n as usize - 1] = b'.';
        }
        result
            .into_iter()
            .map(|row| String::from_utf8(row).unwrap())
            .collect()
    }
}
