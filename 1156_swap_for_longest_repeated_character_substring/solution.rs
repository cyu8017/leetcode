// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

impl Solution {
    pub fn max_rep_opt1(text: String) -> i32 {
        let bytes = text.as_bytes();
        let mut count = [0; 26];
        for &b in bytes {
            count[(b - b'a') as usize] += 1;
        }
        let n = bytes.len();
        let mut ans = 0;
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j < n && bytes[j] == bytes[i] {
                j += 1;
            }
            let length = j - i;
            let mut k = j + 1;
            while k < n && bytes[k] == bytes[i] {
                k += 1;
            }
            let length2 = if j < n { k - j - 1 } else { 0 };
            let mut cand = length + length2 + 1;
            cand = cand.min(count[(bytes[i] - b'a') as usize]);
            ans = ans.max(cand);
            i = j;
        }
        ans as i32
    }
}
