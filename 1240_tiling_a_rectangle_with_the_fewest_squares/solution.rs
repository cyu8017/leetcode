// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

impl Solution {
    pub fn tiling_rectangle(n: i32, m: i32) -> i32 {
        let (n, m) = if n > m { (m, n) } else { (n, m) };
        let n = n as usize;
        let m = m as usize;
        let mut heights = vec![0usize; m];
        let mut best = n * m;
        fn search(n: usize, m: usize, heights: &mut [usize], used: usize, best: &mut usize) {
            if used >= *best {
                return;
            }
            let low = *heights.iter().min().unwrap();
            if low == n {
                *best = used;
                return;
            }
            let left = heights.iter().position(|&h| h == low).unwrap();
            let mut right = left;
            while right < m && heights[right] == low {
                right += 1;
            }
            let max_size = (n - low).min(right - left);
            for size in (1..=max_size).rev() {
                for i in left..left + size {
                    heights[i] = low + size;
                }
                search(n, m, heights, used + 1, best);
                for i in left..left + size {
                    heights[i] = low;
                }
            }
        }
        search(n, m, &mut heights, 0, &mut best);
        best as i32
    }
}
