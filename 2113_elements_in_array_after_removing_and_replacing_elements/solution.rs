// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

impl Solution {
    pub fn element_in_nums(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len() as i32;
        queries
            .into_iter()
            .map(|q| {
                let t = q[0];
                let idx = q[1];
                let cycle = t % (2 * n);
                let (size, offset) = if cycle < n {
                    (n - cycle, cycle)
                } else {
                    (cycle - n, 0)
                };
                if idx >= size {
                    -1
                } else {
                    nums[(offset + idx) as usize]
                }
            })
            .collect()
    }
}
