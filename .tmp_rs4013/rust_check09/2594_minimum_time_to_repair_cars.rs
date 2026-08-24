struct Solution;

// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

impl Solution {
    pub fn repair_cars(ranks: Vec<i32>, cars: i32) -> i64 {
        let cars = cars as i64;
        let ok = |t: i64| {
            let mut done = 0i64;
            for &r in &ranks {
                let mut lo = 0i64;
                let mut hi = cars;
                while lo < hi {
                    let mid = (lo + hi + 1) / 2;
                    if r as i64 * mid * mid <= t {
                        lo = mid;
                    } else {
                        hi = mid - 1;
                    }
                }
                done += lo;
                if done >= cars {
                    return true;
                }
            }
            done >= cars
        };
        let mn = *ranks.iter().min().unwrap() as i64;
        let mut lo = 1i64;
        let mut hi = mn * cars * cars;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}

fn main() {}
