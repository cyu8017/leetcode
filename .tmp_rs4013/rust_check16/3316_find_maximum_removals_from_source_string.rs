struct Solution;
// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

impl Solution {
    pub fn max_removals(source: String, pattern: String, target_indices: Vec<i32>) -> i32 {
        let n = source.len();
        let sb = source.as_bytes();
        let pb = pattern.as_bytes();
        let ok = |remove_first: usize| -> bool {
            let mut mark = vec![false; n];
            for i in 0..remove_first {
                mark[target_indices[i] as usize] = true;
            }
            let mut j = 0;
            for i in 0..n {
                if j >= pb.len() {
                    break;
                }
                if mark[i] {
                    continue;
                }
                if sb[i] == pb[j] {
                    j += 1;
                }
            }
            j == pb.len()
        };
        let mut lo = 0;
        let mut hi = target_indices.len();
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if ok(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}

fn main() {}
