// LeetCode 1473 - Paint House III
// https://leetcode.com/problems/paint-house-iii/

use std::collections::HashMap;

impl Solution {
    pub fn min_cost(
        houses: Vec<i32>,
        cost: Vec<Vec<i32>>,
        _m: i32,
        n: i32,
        target: i32,
    ) -> i32 {
        let inf = i64::MAX / 4;
        let n = n as usize;
        let target = target as i32;
        let mut dp: HashMap<(i32, i32), i64> = HashMap::new();
        dp.insert((0, 0), 0);
        for (i, &painted) in houses.iter().enumerate() {
            let mut nxt = HashMap::new();
            let colors: Vec<i32> = if painted != 0 {
                vec![painted]
            } else {
                (1..=n as i32).collect()
            };
            for (&(prev, groups), &value) in &dp {
                for &color in &colors {
                    let ng = groups + i32::from(color != prev);
                    if ng <= target {
                        let nv = value + if painted != 0 { 0 } else { cost[i][(color - 1) as usize] as i64 };
                        nxt.entry((color, ng))
                            .and_modify(|e| *e = (*e).min(nv))
                            .or_insert(nv);
                    }
                }
            }
            dp = nxt;
        }
        dp.into_iter()
            .filter(|((_, g), _)| *g == target)
            .map(|(_, v)| v)
            .min()
            .map(|v| if v >= inf { -1 } else { v as i32 })
            .unwrap_or(-1)
    }
}
