// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

use std::collections::HashMap;

impl Solution {
    pub fn num_squareful_perms(nums: Vec<i32>) -> i32 {
        let mut count: HashMap<i32, i32> = HashMap::new();
        for &x in &nums {
            *count.entry(x).or_insert(0) += 1;
        }
        let keys: Vec<i32> = count.keys().copied().collect();
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for &a in &keys {
            for &b in &keys {
                let s = a as i64 + b as i64;
                let r = (s as f64).sqrt().round() as i64;
                if r * r == s {
                    graph.entry(a).or_default().push(b);
                }
            }
        }
        fn dfs(
            x: i32,
            remain: i32,
            count: &mut HashMap<i32, i32>,
            graph: &HashMap<i32, Vec<i32>>,
            ans: &mut i32,
        ) {
            if remain == 0 {
                *ans += 1;
                return;
            }
            if let Some(ys) = graph.get(&x).cloned() {
                for y in ys {
                    if *count.get(&y).unwrap_or(&0) > 0 {
                        *count.get_mut(&y).unwrap() -= 1;
                        dfs(y, remain - 1, count, graph, ans);
                        *count.get_mut(&y).unwrap() += 1;
                    }
                }
            }
        }
        let mut ans = 0;
        let remain = nums.len() as i32 - 1;
        let xs: Vec<i32> = count.keys().copied().collect();
        for x in xs {
            *count.get_mut(&x).unwrap() -= 1;
            dfs(x, remain, &mut count, &graph, &mut ans);
            *count.get_mut(&x).unwrap() += 1;
        }
        ans
    }
}
