// LeetCode 1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

impl Solution {
    pub fn max_area(h: i32, w: i32, horizontal_cuts: Vec<i32>, vertical_cuts: Vec<i32>) -> i32 {
        let mut hs = horizontal_cuts;
        let mut vs = vertical_cuts;
        hs.push(0);
        hs.push(h);
        vs.push(0);
        vs.push(w);
        hs.sort_unstable();
        vs.sort_unstable();
        let max_h = hs.windows(2).map(|w| w[1] - w[0]).max().unwrap() as i64;
        let max_v = vs.windows(2).map(|w| w[1] - w[0]).max().unwrap() as i64;
        ((max_h * max_v) % 1_000_000_007) as i32
    }
}
