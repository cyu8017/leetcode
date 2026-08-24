// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

impl Solution {
    fn check_cut(rects: &[Vec<i32>], axis: i32) -> bool {
        let mut arr: Vec<(i32, i32)> = rects
            .iter()
            .map(|r| {
                if axis == 0 {
                    (r[0], r[2])
                } else {
                    (r[1], r[3])
                }
            })
            .collect();
        arr.sort_by(|x, y| x.0.cmp(&y.0).then(x.1.cmp(&y.1)));
        let mut cuts = 0;
        let mut end = arr[0].1;
        for i in 1..arr.len() {
            if arr[i].0 >= end {
                cuts += 1;
                end = arr[i].1;
                if cuts >= 2 {
                    return true;
                }
            } else if arr[i].1 > end {
                end = arr[i].1;
            }
        }
        false
    }

    pub fn check_valid_cuts(_n: i32, rectangles: Vec<Vec<i32>>) -> bool {
        Self::check_cut(&rectangles, 0) || Self::check_cut(&rectangles, 1)
    }
}
