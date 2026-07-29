// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

impl Solution {
    pub fn sample_stats(count: Vec<i32>) -> Vec<f64> {
        let total: i64 = count.iter().map(|&c| c as i64).sum();
        let minimum = count.iter().position(|&c| c > 0).unwrap() as i32;
        let maximum = (0..256).rev().find(|&i| count[i] > 0).unwrap() as i32;
        let mean = count
            .iter()
            .enumerate()
            .map(|(i, &c)| i as f64 * c as f64)
            .sum::<f64>()
            / total as f64;
        let mode = (0..256)
            .max_by_key(|&i| count[i])
            .unwrap() as i32;
        let mid1 = (total + 1) / 2;
        let mid2 = (total + 2) / 2;
        let mut seen = 0i64;
        let mut first = None;
        let mut second = None;
        for (i, &c) in count.iter().enumerate() {
            seen += c as i64;
            if first.is_none() && seen >= mid1 {
                first = Some(i as i32);
            }
            if second.is_none() && seen >= mid2 {
                second = Some(i as i32);
                break;
            }
        }
        let median = (first.unwrap() + second.unwrap()) as f64 / 2.0;
        vec![
            minimum as f64,
            maximum as f64,
            mean,
            median,
            mode as f64,
        ]
    }
}
