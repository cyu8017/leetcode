// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

use std::collections::HashSet;

impl Solution {
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        let row = row as usize;
        let col = col as usize;
        let can = |day: usize| -> bool {
            let blocked: HashSet<(usize, usize)> = cells[..day]
                .iter()
                .map(|c| ((c[0] - 1) as usize, (c[1] - 1) as usize))
                .collect();
            let mut stack: Vec<(usize, usize)> = (0..col)
                .filter(|&c| !blocked.contains(&(0, c)))
                .map(|c| (0, c))
                .collect();
            let mut seen: HashSet<(usize, usize)> = stack.iter().copied().collect();
            while let Some((r, c)) = stack.pop() {
                if r == row - 1 {
                    return true;
                }
                for (nr, nc) in [
                    (r.wrapping_sub(1), c),
                    (r + 1, c),
                    (r, c.wrapping_sub(1)),
                    (r, c + 1),
                ] {
                    if nr < row
                        && nc < col
                        && !blocked.contains(&(nr, nc))
                        && seen.insert((nr, nc))
                    {
                        stack.push((nr, nc));
                    }
                }
            }
            false
        };

        let mut lo = 1i32;
        let mut hi = cells.len() as i32;
        let mut ans = 0i32;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if can(mid as usize) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ans
    }
}
