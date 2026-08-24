// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

use std::collections::HashSet;

impl Solution {
    pub fn max_substring_length(s: String, k: i32) -> bool {
        let n = s.len();
        let bytes = s.as_bytes();
        let mut first = vec![n; 26];
        let mut last = vec![-1i32; 26];
        for i in 0..n {
            let ci = (bytes[i] - b'a') as usize;
            if first[ci] == n {
                first[ci] = i;
            }
            last[ci] = i as i32;
        }
        let mut segs = Vec::new();
        for c in 0..26 {
            if last[c] == -1 {
                continue;
            }
            let mut l = first[c] as i32;
            let mut r = last[c];
            let mut i = l;
            while i <= r {
                let ci = (bytes[i as usize] - b'a') as usize;
                if (first[ci] as i32) < l {
                    l = first[ci] as i32;
                    i = l - 1;
                    i += 1;
                    continue;
                }
                if last[ci] > r {
                    r = last[ci];
                }
                i += 1;
            }
            if !(l == 0 && r == n as i32 - 1) {
                segs.push((l, r));
            }
        }
        let mut uniq = HashSet::new();
        let mut arr = Vec::new();
        for sg in segs {
            if uniq.insert(sg) {
                arr.push(sg);
            }
        }
        arr.sort_by_key(|a| a.1);
        let mut cnt = 0;
        let mut end = -1;
        for sg in arr {
            if sg.0 > end {
                cnt += 1;
                end = sg.1;
            }
        }
        cnt >= k
    }
}
