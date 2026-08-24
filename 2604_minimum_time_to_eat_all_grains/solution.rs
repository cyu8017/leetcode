// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

impl Solution {
    pub fn minimum_time(mut hens: Vec<i32>, mut grains: Vec<i32>) -> i32 {
        hens.sort_unstable();
        grains.sort_unstable();
        let ok = |t: i32| {
            let mut j = 0;
            for &h in &hens {
                if j >= grains.len() {
                    return true;
                }
                if grains[j] >= h {
                    while j < grains.len() && grains[j] - h <= t {
                        j += 1;
                    }
                } else {
                    if h - grains[j] > t {
                        return false;
                    }
                    let left = h - grains[j];
                    let max_right1 = t - 2 * left;
                    let max_right2 = (t - left) / 2;
                    let mut reach = h;
                    if max_right1 > max_right2 {
                        if max_right1 > 0 {
                            reach = h + max_right1;
                        }
                    } else if max_right2 > 0 {
                        reach = h + max_right2;
                    }
                    while j < grains.len() && grains[j] <= reach {
                        j += 1;
                    }
                }
            }
            j >= grains.len()
        };
        let mut lo = 0i32;
        let mut hi = 2_000_000_000i32;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
