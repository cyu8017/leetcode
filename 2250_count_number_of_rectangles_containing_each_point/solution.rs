// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

impl Solution {
    pub fn count_rectangles(rectangles: Vec<Vec<i32>>, points: Vec<Vec<i32>>) -> Vec<i32> {
        let mut by_h: Vec<Vec<i32>> = vec![Vec::new(); 101];
        for r in rectangles {
            by_h[r[1] as usize].push(r[0]);
        }
        for h in 1..=100 {
            by_h[h].sort_unstable();
        }
        let mut ans = vec![0; points.len()];
        for (i, p) in points.iter().enumerate() {
            let x = p[0];
            let y = p[1] as usize;
            let mut cnt = 0;
            for h in y..=100 {
                let xs = &by_h[h];
                let it = xs.partition_point(|&v| v < x);
                cnt += (xs.len() - it) as i32;
            }
            ans[i] = cnt;
        }
        ans
    }
}
