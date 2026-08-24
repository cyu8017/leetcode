// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

impl Solution {
    pub fn min_cost_good_caption(caption: String) -> String {
        let n = caption.len();
        if n < 3 {
            return String::new();
        }
        let cap = caption.as_bytes();
        let mut ans = cap.to_vec();
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j < n && ans[j] == ans[i] {
                j += 1;
            }
            if j - i >= 3 {
                i = j;
                continue;
            }
            let need = 3 - (j - i);
            if j + need <= n {
                for t in 0..need {
                    ans[j + t] = ans[i];
                }
                i = j + need;
            } else {
                let mut ch = b'a';
                if i > 0 {
                    ch = ans[i - 1];
                } else if j < n {
                    ch = cap[j];
                }
                for t in i..n {
                    ans[t] = ch;
                }
                break;
            }
        }
        i = 0;
        while i < n {
            let mut j = i;
            while j < n && ans[j] == ans[i] {
                j += 1;
            }
            if j - i < 3 {
                return String::new();
            }
            i = j;
        }
        String::from_utf8(ans).unwrap()
    }
}
