// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

impl Solution {
    pub fn create_grid(m: i32, n: i32, k: i32) -> Vec<String> {
        let mut cands: Vec<Vec<&str>> = Vec::new();
        if k == 1 {
            cands.push(vec!["."]);
        } else if k == 2 {
            cands.push(vec!["..", ".."]);
        } else if k == 3 {
            cands.push(vec!["..", "..", ".."]);
            cands.push(vec!["...", "..."]);
        } else if k == 4 {
            cands.push(vec!["..", "..", "..", ".."]);
            cands.push(vec!["....", "...."]);
            cands.push(vec!["..#", "...", "#.."]);
        }
        for pat in cands {
            let pr = pat.len();
            let pc = pat[0].len();
            if pr > m as usize || pc > n as usize {
                continue;
            }
            let mut result = vec![vec![b'#'; n as usize]; m as usize];
            for i in 0..pr {
                let row = pat[i].as_bytes();
                for j in 0..pc {
                    result[i][j] = row[j];
                }
            }
            for i in pr..m as usize {
                result[i][pc - 1] = b'.';
            }
            for j in pc..n as usize {
                result[m as usize - 1][j] = b'.';
            }
            return result
                .into_iter()
                .map(|row| String::from_utf8(row).unwrap())
                .collect();
        }
        vec![]
    }
}
