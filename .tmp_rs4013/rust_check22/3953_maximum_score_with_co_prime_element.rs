struct Solution;
// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

impl Solution {
    pub fn max_score(nums: Vec<i32>, max_val: i32) -> i32 {
        let mut limit = max_val;
        let mut frequency = vec![0; 100001];
        for &x in &nums {
            frequency[x as usize] += 1;
            if x > limit {
                limit = x;
            }
        }
        let mut divisible = vec![0; (limit + 1) as usize];
        for d in 1..=limit {
            let mut multiple = d;
            while multiple <= limit {
                if (multiple as usize) < frequency.len() {
                    divisible[d as usize] += frequency[multiple as usize];
                }
                multiple += d;
            }
        }
        let bad_count = |x: i32| -> i32 {
            let mut primes = Vec::new();
            let mut y = x;
            let mut p = 2;
            while p as i64 * p as i64 <= y as i64 {
                if y % p == 0 {
                    primes.push(p);
                    while y % p == 0 {
                        y /= p;
                    }
                }
                p += 1;
            }
            if y > 1 {
                primes.push(y);
            }
            let mut bad = 0;
            let psz = primes.len();
            for mask in 1..(1 << psz) {
                let mut product = 1;
                let mut bits = 0;
                for i in 0..psz {
                    if (mask >> i) & 1 == 1 {
                        product *= primes[i];
                        bits += 1;
                    }
                }
                if bits % 2 == 1 {
                    bad += divisible[product as usize];
                } else {
                    bad -= divisible[product as usize];
                }
            }
            bad
        };
        let mut best = -(nums.len() as i32);
        let mut checked = vec![false; (limit + 1) as usize];
        let mut evaluate = |x: i32, exists: bool| {
            if checked[x as usize] {
                return;
            }
            checked[x as usize] = true;
            let bad = bad_count(x);
            let cost = if exists {
                if x > 1 {
                    bad - 1
                } else {
                    0
                }
            } else if bad > 0 {
                bad
            } else {
                1
            };
            if x - cost > best {
                best = x - cost;
            }
        };
        for x in 1..=max_val {
            evaluate(x, (x as usize) < frequency.len() && frequency[x as usize] > 0);
        }
        for &x in &nums {
            evaluate(x, true);
        }
        best
    }
}

fn main() {}
