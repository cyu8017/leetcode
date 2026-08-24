// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

impl Solution {
    pub fn max_product(s: String) -> i32 {
        let chars: Vec<u8> = s.bytes().collect();
        let n = chars.len();
        let is_pal = |mask: i32| -> (bool, i32) {
            let mut seq = Vec::new();
            for i in 0..n {
                if mask & (1 << i) != 0 {
                    seq.push(chars[i]);
                }
            }
            let mut l = 0;
            let mut r = seq.len() as i32 - 1;
            while l < r {
                if seq[l as usize] != seq[r as usize] {
                    return (false, 0);
                }
                l += 1;
                r -= 1;
            }
            (true, seq.len() as i32)
        };
        let mut best = 0;
        let total = 1 << n;
        for mask1 in 1..total {
            let (ok1, len1) = is_pal(mask1);
            if !ok1 {
                continue;
            }
            let remain = (total - 1) ^ mask1;
            let mut mask2 = remain;
            while mask2 > 0 {
                let (ok2, len2) = is_pal(mask2);
                if ok2 && len1 * len2 > best {
                    best = len1 * len2;
                }
                mask2 = (mask2 - 1) & remain;
            }
        }
        best
    }
}
