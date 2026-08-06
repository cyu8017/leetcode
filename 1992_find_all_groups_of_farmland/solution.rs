// LeetCode 1992 - Find All Groups of Farmland
// https://leetcode.com/problems/find-all-groups-of-farmland/

impl Solution {
    pub fn find_farmland(land: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = land.len();
        let n = land[0].len();
        let mut ans = Vec::new();
        for i in 0..m {
            for j in 0..n {
                if land[i][j] == 1
                    && (i == 0 || land[i - 1][j] == 0)
                    && (j == 0 || land[i][j - 1] == 0)
                {
                    let mut r = i;
                    let mut c = j;
                    while r + 1 < m && land[r + 1][j] == 1 {
                        r += 1;
                    }
                    while c + 1 < n && land[i][c + 1] == 1 {
                        c += 1;
                    }
                    ans.push(vec![i as i32, j as i32, r as i32, c as i32]);
                }
            }
        }
        ans
    }
}
