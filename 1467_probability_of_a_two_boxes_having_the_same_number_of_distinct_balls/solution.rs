// LeetCode 1467 - Probability of a Two Boxes Having the Same Number of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

impl Solution {
    fn comb(n: i64, k: i64) -> i64 {
        if k < 0 || k > n {
            return 0;
        }
        let mut res = 1i64;
        for i in 0..k {
            res = res * (n - i) / (i + 1);
        }
        res
    }

    pub fn get_probability(balls: Vec<i32>) -> f64 {
        let half = balls.iter().sum::<i32>() / 2;
        let mut good = 0i64;
        let mut total = 0i64;
        Self::dfs(0, 0, 0, 1, &balls, half, &mut good, &mut total);
        good as f64 / total as f64
    }

    fn dfs(
        i: usize,
        left: i32,
        dl: i32,
        ways: i64,
        balls: &[i32],
        half: i32,
        good: &mut i64,
        total: &mut i64,
    ) {
        if i == balls.len() {
            if left == half {
                *total += ways;
                if dl == 0 {
                    *good += ways;
                }
            }
            return;
        }
        for x in 0..=balls[i] {
            if left + x <= half {
                let ndl = dl + i32::from(x > 0) - i32::from(x < balls[i]);
                Self::dfs(
                    i + 1,
                    left + x,
                    ndl,
                    ways * Self::comb(balls[i] as i64, x as i64),
                    balls,
                    half,
                    good,
                    total,
                );
            }
        }
    }
}
