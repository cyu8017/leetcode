struct Solution;
// LeetCode 4009 - Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

use std::collections::HashMap;

fn pack_key(i: i32, f0: i32, f1: i32, d0: i32, d1: i32) -> i64 {
    ((((i as i64 * 51 + f0 as i64) * 51 + f1 as i64) * 21 + d0 as i64) * 21) + d1 as i64
}

fn max_serve(
    i: i32,
    f0: i32,
    f1: i32,
    d0: i32,
    d1: i32,
    n: i32,
    dem: &[i32],
    memo: &mut HashMap<i64, i32>,
) -> i32 {
    if i == n {
        return i;
    }
    let key = pack_key(i, f0, f1, d0, d1);
    if let Some(&v) = memo.get(&key) {
        return v;
    }
    let need = dem[i as usize];
    let can0 = f0 >= need;
    let can1 = f1 >= need;
    let mut best = i;
    if !can0 && !can1 {
        memo.insert(key, best);
        return best;
    }
    if can0 {
        let nd1 = if d1 > d0 { d1 - d0 } else { 0 };
        best = best.max(max_serve(i + 1, f0 - need, f1, need, nd1, n, dem, memo));
    }
    if can1 {
        let nd0 = if d0 > d1 { d0 - d1 } else { 0 };
        best = best.max(max_serve(i + 1, f0, f1 - need, nd0, need, n, dem, memo));
    }
    memo.insert(key, best);
    best
}

fn can_with_w(
    i: i32,
    f0: i32,
    f1: i32,
    d0: i32,
    d1: i32,
    n: i32,
    w: i32,
    best_serve: i32,
    dem: &[i32],
    memo: &mut HashMap<i64, i32>,
) -> bool {
    if i >= best_serve {
        return true;
    }
    if i == n {
        return true;
    }
    let key = pack_key(i, f0, f1, d0, d1);
    if let Some(&v) = memo.get(&key) {
        return v == 2;
    }
    let need = dem[i as usize];
    let can0 = f0 >= need;
    let can1 = f1 >= need;
    let mut ok = false;
    if !can0 && !can1 {
        memo.insert(key, 1);
        return false;
    }
    if can0 && d0 <= w {
        let nd1 = if d1 > d0 { d1 - d0 } else { 0 };
        if can_with_w(i + 1, f0 - need, f1, need, nd1, n, w, best_serve, dem, memo) {
            ok = true;
        }
    }
    if !ok && can1 && d1 <= w {
        let nd0 = if d0 > d1 { d0 - d1 } else { 0 };
        if can_with_w(i + 1, f0, f1 - need, nd0, need, n, w, best_serve, dem, memo) {
            ok = true;
        }
    }
    memo.insert(key, if ok { 2 } else { 1 });
    ok
}

impl Solution {
    pub fn min_max_waiting_time(demand: Vec<i32>, fuel: Vec<i32>) -> i32 {
        let n = demand.len() as i32;
        let f0 = fuel[0];
        let f1 = fuel[1];
        if f0 < demand[0] && f1 < demand[0] {
            return -1;
        }
        let mut memo = HashMap::new();
        let best_serve = max_serve(0, f0, f1, 0, 0, n, &demand, &mut memo);
        if best_serve == 0 {
            return -1;
        }
        let mut lo = 0;
        let mut hi = demand.iter().sum::<i32>();
        let mut ans = hi;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            memo.clear();
            if can_with_w(0, f0, f1, 0, 0, n, mid, best_serve, &demand, &mut memo) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        ans
    }
}

fn main() {}
