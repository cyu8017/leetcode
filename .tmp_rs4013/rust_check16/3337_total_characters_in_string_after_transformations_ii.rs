struct Solution;
// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

impl Solution {
    fn mat_mul(a: &[Vec<i32>], b: &[Vec<i32>], modulus: i64) -> Vec<Vec<i32>> {
        let n = a.len();
        let mut c = vec![vec![0i32; n]; n];
        for i in 0..n {
            for k in 0..n {
                if a[i][k] == 0 {
                    continue;
                }
                for j in 0..n {
                    c[i][j] = ((c[i][j] as i64 + a[i][k] as i64 * b[k][j] as i64 % modulus) % modulus) as i32;
                }
            }
        }
        c
    }

    fn mat_pow(mut a: Vec<Vec<i32>>, mut e: i32, modulus: i64) -> Vec<Vec<i32>> {
        let n = a.len();
        let mut r = vec![vec![0i32; n]; n];
        for i in 0..n {
            r[i][i] = 1;
        }
        while e > 0 {
            if e & 1 == 1 {
                r = Self::mat_mul(&r, &a, modulus);
            }
            a = Self::mat_mul(&a, &a, modulus);
            e >>= 1;
        }
        r
    }

    pub fn length_after_transformations(s: String, t: i32, nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut mat = vec![vec![0i32; 26]; 26];
        for i in 0..26 {
            for j in 1..=nums[i] {
                mat[i][(i + j as usize) % 26] = 1;
            }
        }
        mat = Self::mat_pow(mat, t, MOD);
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let mut ans = 0i32;
        for i in 0..26 {
            for j in 0..26 {
                ans = ((ans as i64 + cnt[i] as i64 * mat[i][j] as i64 % MOD) % MOD) as i32;
            }
        }
        ans
    }
}

fn main() {}
