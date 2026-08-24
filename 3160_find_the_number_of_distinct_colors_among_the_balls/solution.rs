// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

use std::collections::HashMap;

impl Solution {
    pub fn query_results(_limit: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut g: HashMap<i32, i32> = HashMap::new();
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let (x, y) = (q[0], q[1]);
            *cnt.entry(y).or_insert(0) += 1;
            if let Some(&old) = g.get(&x) {
                let e = cnt.get_mut(&old).unwrap();
                *e -= 1;
                if *e == 0 {
                    cnt.remove(&old);
                }
            }
            g.insert(x, y);
            ans.push(cnt.len() as i32);
        }
        ans
    }
}
