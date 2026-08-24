struct Solution;
// LeetCode 3398 - Smallest Substring With Identical Characters I
// https://leetcode.com/problems/smallest-substring-with-identical-characters-i/

impl Solution {
    pub fn min_length(s: String, num_ops: i32) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes();
        let ok = |l: i32| -> bool {
            if l == 0 {
                return false;
            }
            let mut ops = 0;
            let mut i = 0;
            while i < n {
                let mut j = i;
                while j < n && bytes[j] == bytes[i] {
                    j += 1;
                }
                ops += (j - i) as i32 / (l + 1);
                i = j;
            }
            ops <= num_ops
        };
        let mut lo = 1;
        let mut hi = n as i32;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}

fn main() {}
