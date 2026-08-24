// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

impl Solution {
    pub fn flip_and_invert_image(mut image: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        for row in &mut image {
            row.reverse();
            for x in row.iter_mut() {
                *x = 1 - *x;
            }
        }
        image
    }
}
