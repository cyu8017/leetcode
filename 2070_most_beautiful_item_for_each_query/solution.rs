// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

impl Solution {
    pub fn maximum_beauty(mut items: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        items.sort_unstable();
        let mut max_b = 0;
        for it in &mut items {
            max_b = max_b.max(it[1]);
            it[1] = max_b;
        }
        let mut ans = vec![0; queries.len()];
        for (i, &q) in queries.iter().enumerate() {
            let mut lo = 0;
            let mut hi = items.len();
            while lo < hi {
                let mid = (lo + hi) / 2;
                if items[mid][0] <= q {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            ans[i] = if lo == 0 { 0 } else { items[lo - 1][1] };
        }
        ans
    }
}
