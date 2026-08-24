// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/

impl Solution {
    pub fn smallest_unique_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut sa: Vec<usize> = (0..n).collect();
        let mut rank = nums.clone();
        let mut width = 1;
        while width < n {
            sa.sort_by(|&a, &b| {
                if rank[a] != rank[b] {
                    return rank[a].cmp(&rank[b]);
                }
                let ra = if a + width < n { rank[a + width] } else { -1 };
                let rb = if b + width < n { rank[b + width] } else { -1 };
                ra.cmp(&rb)
            });
            let mut next = vec![0; n];
            for i in 1..n {
                let a = sa[i - 1];
                let b = sa[i];
                let different = rank[a] != rank[b];
                let ra = if a + width < n { rank[a + width] } else { -1 };
                let rb = if b + width < n { rank[b + width] } else { -1 };
                next[b] = if different || ra != rb {
                    next[a] + 1
                } else {
                    next[a]
                };
            }
            rank = next;
            if rank[sa[n - 1]] == n as i32 - 1 {
                break;
            }
            width <<= 1;
        }
        let mut pos = vec![0; n];
        for i in 0..n {
            pos[sa[i]] = i;
        }
        let mut lcp = vec![0; n.saturating_sub(1)];
        let mut height = 0i32;
        for i in 0..n {
            let p = pos[i];
            if p == n - 1 {
                height = 0;
                continue;
            }
            let j = sa[p + 1];
            while i + (height as usize) < n
                && j + (height as usize) < n
                && nums[i + height as usize] == nums[j + height as usize]
            {
                height += 1;
            }
            lcp[p] = height;
            if height > 0 {
                height -= 1;
            }
        }
        let mut ans = n as i32;
        for p in 0..n {
            let start = sa[p];
            let mut need = 1;
            if p > 0 && lcp[p - 1] + 1 > need {
                need = lcp[p - 1] + 1;
            }
            if p + 1 < n && lcp[p] + 1 > need {
                need = lcp[p] + 1;
            }
            if need <= (n - start) as i32 && need < ans {
                ans = need;
            }
        }
        ans
    }
}
