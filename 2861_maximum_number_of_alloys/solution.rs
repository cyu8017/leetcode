// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

impl Solution {
    pub fn max_number_of_alloys(
        n: i32,
        _k: i32,
        budget: i32,
        composition: Vec<Vec<i32>>,
        stock: Vec<i32>,
        cost: Vec<i32>,
    ) -> i32 {
        let n = n as usize;
        let ok = |machines: i64| -> bool {
            for comp in &composition {
                let mut spend = 0i64;
                for i in 0..n {
                    let need = machines * comp[i] as i64 - stock[i] as i64;
                    if need > 0 {
                        spend += need * cost[i] as i64;
                    }
                }
                if spend <= budget as i64 {
                    return true;
                }
            }
            false
        };
        let mut lo = 0i64;
        let mut hi = 1_000_000_000i64;
        let mut ans = 0i64;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ans as i32
    }
}
