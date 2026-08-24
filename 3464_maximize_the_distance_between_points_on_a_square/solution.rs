// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

impl Solution {
    fn can_place(arr: &[i32], perim: i32, k: i32, mid: i32) -> bool {
        let n = arr.len();
        for s in 0..n {
            let mut cnt = 1;
            let mut last = arr[s];
            let mut idx = s;
            while cnt < k {
                let target = last + mid;
                let mut found = false;
                for step in 1..n {
                    let ni = (idx + step) % n;
                    let val = arr[ni];
                    let add = if ni <= idx { perim } else { 0 };
                    if val + add >= target {
                        last = val + add;
                        idx = ni;
                        cnt += 1;
                        found = true;
                        break;
                    }
                }
                if !found {
                    break;
                }
            }
            if cnt == k && last - arr[s] <= perim - mid {
                return true;
            }
        }
        false
    }

    pub fn max_distance(side: i32, points: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut arr = vec![0; points.len()];
        for i in 0..points.len() {
            let x = points[i][0];
            let y = points[i][1];
            arr[i] = if y == 0 {
                x
            } else if x == side {
                side + y
            } else if y == side {
                2 * side + (side - x)
            } else {
                3 * side + (side - y)
            };
        }
        arr.sort_unstable();
        let perim = 4 * side;
        let mut lo = 0;
        let mut hi = 2 * side;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if Self::can_place(&arr, perim, k, mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}
