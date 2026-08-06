// LeetCode 1504 - Count Submatrices with All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

impl Solution {
    pub fn num_submat(mat: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        let mut heights = vec![0; mat[0].len()];
        for row in &mat {
            for (j, &x) in row.iter().enumerate() {
                heights[j] = if x == 0 { 0 } else { heights[j] + 1 };
            }
            let mut stack: Vec<(i32, i32)> = Vec::new();
            let mut running = 0;
            for &h in &heights {
                let mut count = 1;
                while stack.last().map_or(false, |&(oh, _)| oh >= h) {
                    let (old, width) = stack.pop().unwrap();
                    running -= old * width;
                    count += width;
                }
                stack.push((h, count));
                running += h * count;
                ans += running;
            }
        }
        ans
    }
}
