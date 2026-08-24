// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

impl Solution {
    pub fn base_unit_conversions(conversions: Vec<Vec<i32>>) -> Vec<i32> {
        let n = conversions.len() + 1;
        let mut g = vec![Vec::<(usize, i32)>::new(); n];
        for e in &conversions {
            g[e[0] as usize].push((e[1] as usize, e[2]));
        }
        let mut ans = vec![0; n];
        fn dfs(s: usize, mul: i32, g: &[Vec<(usize, i32)>], ans: &mut [i32]) {
            ans[s] = mul;
            for &(t, w) in &g[s] {
                dfs(t, ((mul as i64 * w as i64) % 1_000_000_007) as i32, g, ans);
            }
        }
        dfs(0, 1, &g, &mut ans);
        ans
    }
}
