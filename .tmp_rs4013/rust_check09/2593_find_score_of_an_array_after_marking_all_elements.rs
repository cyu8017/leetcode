struct Solution;

// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

impl Solution {
    pub fn find_score(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by(|&a, &b| nums[a].cmp(&nums[b]).then(a.cmp(&b)));
        let mut marked = vec![false; n];
        let mut ans = 0i64;
        for i in idx {
            if marked[i] {
                continue;
            }
            ans += nums[i] as i64;
            marked[i] = true;
            if i > 0 {
                marked[i - 1] = true;
            }
            if i + 1 < n {
                marked[i + 1] = true;
            }
        }
        ans
    }
}

fn main() {}
