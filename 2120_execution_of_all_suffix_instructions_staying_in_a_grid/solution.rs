// LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

impl Solution {
    pub fn execute_instructions(n: i32, start_pos: Vec<i32>, s: String) -> Vec<i32> {
        let m = s.len();
        let s = s.as_bytes();
        let mut ans = vec![0; m];
        for i in 0..m {
            let mut r = start_pos[0];
            let mut c = start_pos[1];
            let mut cnt = 0;
            for j in i..m {
                match s[j] {
                    b'L' => c -= 1,
                    b'R' => c += 1,
                    b'U' => r -= 1,
                    _ => r += 1,
                }
                if r < 0 || r >= n || c < 0 || c >= n {
                    break;
                }
                cnt += 1;
            }
            ans[i] = cnt;
        }
        ans
    }
}
