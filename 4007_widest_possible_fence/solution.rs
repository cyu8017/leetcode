// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_width(planks: Vec<i32>) -> i32 {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for x in planks {
            *cnt.entry(x).or_insert(0) += 1;
        }
        let mut t: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0;
        let pairs: Vec<(i32, i32)> = cnt.iter().map(|(&x, &v)| (x, v)).collect();
        for &(x, v1) in &pairs {
            *t.entry(x).or_insert(0) += v1;
            ans = ans.max(t[&x]);
            *t.entry(x * 2).or_insert(0) += v1 / 2;
            ans = ans.max(t[&(x * 2)]);
            for &(y, v2) in &pairs {
                if y > x {
                    let key = x + y;
                    *t.entry(key).or_insert(0) += v1.min(v2);
                    ans = ans.max(t[&key]);
                }
            }
        }
        ans
    }
}
