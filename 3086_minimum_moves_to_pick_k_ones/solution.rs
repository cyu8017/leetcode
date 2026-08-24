// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

impl Solution {
    pub fn minimum_moves(nums: Vec<i32>, k: i32, max_changes: i32) -> i64 {
        let n = nums.len();
        let mut cnt = vec![0i32; n + 1];
        let mut s = vec![0i64; n + 1];
        for i in 1..=n {
            cnt[i] = cnt[i - 1] + nums[i - 1];
            s[i] = s[i - 1] + i as i64 * nums[i - 1] as i64;
        }
        let mut ans = i64::MAX;
        for i in 1..=n {
            let mut t = 0i64;
            let mut need = k - nums[i - 1];
            for j in [i as i32 - 1, i as i32 + 1] {
                if need > 0 && 1 <= j && j <= n as i32 && nums[j as usize - 1] == 1 {
                    need -= 1;
                    t += 1;
                }
            }
            let c = need.min(max_changes);
            need -= c;
            t += c as i64 * 2;
            if need <= 0 {
                ans = ans.min(t);
                continue;
            }
            let mut l = 2i32;
            let mut r = (i as i32 - 1).max(n as i32 - i as i32);
            while l <= r {
                let mid = (l + r) >> 1;
                let l1 = 1.max(i as i32 - mid) as usize;
                let r1 = 0.max(i as i32 - 2) as usize;
                let l2 = (n as i32 + 1).min(i as i32 + 2) as usize;
                let r2 = (n as i32).min(i as i32 + mid) as usize;
                let c1 = cnt[r1] - cnt[l1 - 1];
                let c2 = cnt[r2] - cnt[l2 - 1];
                if c1 + c2 >= need {
                    let t1 = c1 as i64 * i as i64 - (s[r1] - s[l1 - 1]);
                    let t2 = s[r2] - s[l2 - 1] - c2 as i64 * i as i64;
                    ans = ans.min(t + t1 + t2);
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
        }
        ans
    }
}
