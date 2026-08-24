// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

use std::collections::HashMap;

impl Solution {
    pub fn max_walls(robots: Vec<i32>, distance: Vec<i32>, mut walls: Vec<i32>) -> i32 {
        let n = robots.len();
        let mut arr: Vec<(i32, i32)> = robots.into_iter().zip(distance).collect();
        arr.sort_unstable();
        walls.sort_unstable();
        let mut f: HashMap<(i32, i32), i32> = HashMap::new();
        fn lb(walls: &[i32], x: i32) -> usize {
            walls.partition_point(|&w| w < x)
        }
        fn dfs(
            i: i32,
            j: i32,
            arr: &[(i32, i32)],
            walls: &[i32],
            f: &mut HashMap<(i32, i32), i32>,
        ) -> i32 {
            if i < 0 {
                return 0;
            }
            if let Some(&v) = f.get(&(i, j)) {
                return v;
            }
            let n = arr.len();
            let iu = i as usize;
            let mut left = arr[iu].0 - arr[iu].1;
            if i > 0 {
                left = left.max(arr[iu - 1].0 + 1);
            }
            let l = lb(walls, left);
            let r = lb(walls, arr[iu].0 + 1);
            let mut ans = dfs(i - 1, 0, arr, walls, f) + (r - l) as i32;
            let mut right = arr[iu].0 + arr[iu].1;
            if iu + 1 < n {
                if j == 0 {
                    right = right.min(arr[iu + 1].0 - arr[iu + 1].1 - 1);
                } else {
                    right = right.min(arr[iu + 1].0 - 1);
                }
            }
            let l = lb(walls, arr[iu].0);
            let r = lb(walls, right + 1);
            ans = ans.max(dfs(i - 1, 1, arr, walls, f) + (r - l) as i32);
            f.insert((i, j), ans);
            ans
        }
        dfs(n as i32 - 1, 1, &arr, &walls, &mut f)
    }
}
