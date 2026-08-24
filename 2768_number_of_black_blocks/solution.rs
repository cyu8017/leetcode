// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

use std::collections::HashMap;

impl Solution {
    pub fn count_black_blocks(m: i32, n: i32, coordinates: Vec<Vec<i32>>) -> Vec<i64> {
        let mut cnt: HashMap<(i32, i32), i32> = HashMap::new();
        for c in coordinates {
            let (x, y) = (c[0], c[1]);
            for i in x - 1..=x {
                for j in y - 1..=y {
                    if i >= 0 && j >= 0 && i < m - 1 && j < n - 1 {
                        *cnt.entry((i, j)).or_insert(0) += 1;
                    }
                }
            }
        }
        let mut ans = vec![0i64; 5];
        ans[0] = (m as i64 - 1) * (n as i64 - 1);
        for &v in cnt.values() {
            ans[v as usize] += 1;
            ans[0] -= 1;
        }
        ans
    }
}
