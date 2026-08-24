// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

impl Solution {
    pub fn minimum_partition(s: String, k: i32) -> i32 {
        let k = k as i64;
        let mut ans = 1;
        let mut cur = 0i64;
        for ch in s.bytes() {
            let d = (ch - b'0') as i64;
            if d > k {
                return -1;
            }
            let nxt = cur * 10 + d;
            if nxt > k {
                ans += 1;
                cur = d;
            } else {
                cur = nxt;
            }
        }
        ans
    }
}
