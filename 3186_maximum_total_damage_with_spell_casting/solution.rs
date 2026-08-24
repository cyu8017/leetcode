// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_total_damage(mut power: Vec<i32>) -> i64 {
        let n = power.len();
        power.sort_unstable();
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut nxt = vec![0; n];
        for i in 0..n {
            *cnt.entry(power[i]).or_insert(0) += 1;
            nxt[i] = power.partition_point(|&x| x < power[i] + 3);
        }
        let mut f = vec![None; n];
        fn dfs(
            i: usize,
            n: usize,
            power: &[i32],
            cnt: &HashMap<i32, i32>,
            nxt: &[usize],
            f: &mut [Option<i64>],
        ) -> i64 {
            if i >= n {
                return 0;
            }
            if let Some(v) = f[i] {
                return v;
            }
            let c = *cnt.get(&power[i]).unwrap() as usize;
            let a = dfs(i + c, n, power, cnt, nxt, f);
            let b = power[i] as i64 * c as i64 + dfs(nxt[i], n, power, cnt, nxt, f);
            let res = a.max(b);
            f[i] = Some(res);
            res
        }
        dfs(0, n, &power, &cnt, &nxt, &mut f)
    }
}
