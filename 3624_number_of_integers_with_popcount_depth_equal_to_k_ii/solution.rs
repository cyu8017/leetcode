// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

impl Solution {
    fn depth(mut x: i64) -> i32 {
        if x == 1 {
            return 0;
        }
        let mut d = 0;
        while x > 1 {
            x = x.count_ones() as i64;
            d += 1;
        }
        d
    }

    pub fn popcount_depth(nums: Vec<i64>, queries: Vec<Vec<i64>>) -> Vec<i32> {
        let mut a = nums;
        let mut ans = Vec::new();
        for q in queries {
            if q[0] == 1 {
                let l = q[1] as usize;
                let r = q[2] as usize;
                let k = q[3] as i32;
                let mut cnt = 0;
                for i in l..=r {
                    if Self::depth(a[i]) == k {
                        cnt += 1;
                    }
                }
                ans.push(cnt);
            } else {
                a[q[1] as usize] = q[2];
            }
        }
        ans
    }
}
