// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

impl Solution {
    pub fn min_wasted_space(mut packages: Vec<i32>, boxes: Vec<Vec<i32>>) -> i32 {
        packages.sort_unstable();
        let mut prefix = vec![0i64; packages.len()];
        prefix[0] = packages[0] as i64;
        for i in 1..packages.len() {
            prefix[i] = prefix[i - 1] + packages[i] as i64;
        }
        let mut answer = i64::MAX;
        for mut supplier in boxes {
            supplier.sort_unstable();
            let mut start = 0usize;
            let mut wasted = 0i64;
            for &box_size in &supplier {
                let mut lo = start;
                let mut hi = packages.len();
                while lo < hi {
                    let mid = (lo + hi) / 2;
                    if packages[mid] <= box_size {
                        lo = mid + 1;
                    } else {
                        hi = mid;
                    }
                }
                let end = lo;
                if end == start {
                    continue;
                }
                let package_sum = prefix[end - 1] - if start > 0 { prefix[start - 1] } else { 0 };
                wasted += box_size as i64 * (end - start) as i64 - package_sum;
                start = end;
            }
            if start == packages.len() {
                answer = answer.min(wasted);
            }
        }
        if answer == i64::MAX {
            -1
        } else {
            (answer % 1_000_000_007) as i32
        }
    }
}
