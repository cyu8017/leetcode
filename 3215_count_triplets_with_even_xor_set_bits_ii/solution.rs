// LeetCode 3215 - Count Triplets with Even XOR Set Bits II
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

impl Solution {
    pub fn triplet_count(a: Vec<i32>, b: Vec<i32>, c: Vec<i32>) -> i64 {
        let mut cnt1 = [0i64; 2];
        let mut cnt2 = [0i64; 2];
        let mut cnt3 = [0i64; 2];
        for x in a {
            cnt1[(x.count_ones() % 2) as usize] += 1;
        }
        for x in b {
            cnt2[(x.count_ones() % 2) as usize] += 1;
        }
        for x in c {
            cnt3[(x.count_ones() % 2) as usize] += 1;
        }
        let mut ans = 0i64;
        for i in 0..2 {
            for j in 0..2 {
                for k in 0..2 {
                    if (i + j + k) % 2 == 0 {
                        ans += cnt1[i] * cnt2[j] * cnt3[k];
                    }
                }
            }
        }
        ans
    }
}
