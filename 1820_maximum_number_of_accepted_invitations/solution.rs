// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

impl Solution {
    pub fn maximum_invitations(grid: Vec<Vec<i32>>) -> i32 {
        let boys = grid.len();
        let girls = grid[0].len();
        let mut match_girl = vec![-1i32; girls];

        fn dfs(
            boy: usize,
            grid: &[Vec<i32>],
            match_girl: &mut [i32],
            seen: &mut [bool],
        ) -> bool {
            let girls = grid[0].len();
            for girl in 0..girls {
                if grid[boy][girl] != 0 && !seen[girl] {
                    seen[girl] = true;
                    let matched = match_girl[girl];
                    if matched == -1 || dfs(matched as usize, grid, match_girl, seen) {
                        match_girl[girl] = boy as i32;
                        return true;
                    }
                }
            }
            false
        }

        let mut ans = 0;
        for boy in 0..boys {
            let mut seen = vec![false; girls];
            if dfs(boy, &grid, &mut match_girl, &mut seen) {
                ans += 1;
            }
        }
        ans
    }
}
