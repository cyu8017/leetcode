struct Solution;
// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    fn sieve(n: usize) -> Vec<bool> {
        let mut is_p = vec![false; n];
        for i in 2..n {
            is_p[i] = true;
        }
        let mut i = 2;
        while i * i < n {
            if is_p[i] {
                let mut j = i * i;
                while j < n {
                    is_p[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        is_p
    }

    pub fn min_operations(n: i32, m: i32) -> i32 {
        let is_prime = Self::sieve(100000);
        if is_prime[n as usize] {
            return -1;
        }
        let mut dist = vec![-1; 100000];
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((n, n)));
        dist[n as usize] = n;
        while let Some(Reverse((cost, val))) = pq.pop() {
            if cost != dist[val as usize] {
                continue;
            }
            if val == m {
                return cost;
            }
            let mut s: Vec<u8> = val.to_string().into_bytes();
            for i in 0..s.len() {
                let orig = s[i];
                for d in [-1, 1] {
                    let nd = orig as i32 - b'0' as i32 + d;
                    if nd < 0 || nd > 9 {
                        continue;
                    }
                    if i == 0 && nd == 0 && s.len() > 1 {
                        continue;
                    }
                    s[i] = b'0' + nd as u8;
                    let nv: i32 = String::from_utf8(s.clone()).unwrap().parse().unwrap();
                    s[i] = orig;
                    if is_prime[nv as usize] {
                        continue;
                    }
                    let nc = cost + nv;
                    if dist[nv as usize] == -1 || nc < dist[nv as usize] {
                        dist[nv as usize] = nc;
                        pq.push(Reverse((nc, nv)));
                    }
                }
            }
        }
        -1
    }
}

fn main() {}
