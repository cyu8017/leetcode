// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

impl Solution {
    pub fn special_grid(n: i32) -> Vec<Vec<i32>> {
        let m = 1usize << n;
        let mut ans = vec![vec![0; m]; m];
        let mut val = 0;
        fn dfs(x: i32, y: i32, k: i32, ans: &mut [Vec<i32>], val: &mut i32) {
            if k == 1 {
                ans[x as usize][y as usize] = *val;
                *val += 1;
                return;
            }
            let h = k / 2;
            dfs(x, y, h, ans, val);
            dfs(x + h, y, h, ans, val);
            dfs(x + h, y - h, h, ans, val);
            dfs(x, y - h, h, ans, val);
        }
        dfs(0, m as i32 - 1, m as i32, &mut ans, &mut val);
        ans
    }
}
