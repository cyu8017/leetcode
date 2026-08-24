// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

impl Solution {
    pub fn maximum_length(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut groups: [Vec<i32>; 26] = Default::default();
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j < n && b[j] == b[i] {
                j += 1;
            }
            groups[(b[i] - b'a') as usize].push((j - i) as i32);
            i = j;
        }
        let mut ans = -1;
        for arr in groups.iter_mut() {
            if arr.is_empty() {
                continue;
            }
            arr.sort_unstable_by(|a, b| b.cmp(a));
            for l in (1..=arr[0]).rev() {
                let mut cnt = 0;
                for &g in arr.iter() {
                    if g >= l {
                        cnt += g - l + 1;
                    }
                }
                if cnt >= 3 {
                    if l > ans {
                        ans = l;
                    }
                    break;
                }
            }
        }
        ans
    }
}
