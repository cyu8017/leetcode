// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

impl Solution {
    pub fn component_value(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let total: i32 = nums.iter().sum();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        fn dfs(u: usize, p: i32, target: i32, nums: &[i32], g: &[Vec<usize>]) -> i32 {
            let mut sum = nums[u];
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let sub = dfs(v, u as i32, target, nums, g);
                if sub < 0 {
                    return -1;
                }
                sum += sub;
            }
            if sum > target {
                return -1;
            }
            if sum == target {
                return 0;
            }
            sum
        }
        for parts in (1..=n as i32).rev() {
            if total % parts != 0 {
                continue;
            }
            let target = total / parts;
            if dfs(0, -1, target, &nums, &g) == 0 {
                return parts - 1;
            }
        }
        0
    }
}
