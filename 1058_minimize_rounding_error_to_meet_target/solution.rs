// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

impl Solution {
    pub fn minimize_error(prices: Vec<String>, target: i32) -> String {
        let mut floors = 0i32;
        let mut fracs: Vec<f64> = Vec::new();
        for p in &prices {
            let value: f64 = p.parse().unwrap();
            let floor = value.floor() as i32;
            floors += floor;
            let frac = value - floor as f64;
            if frac > 1e-9 {
                fracs.push(frac);
            }
        }
        let ceil_count = target - floors;
        if ceil_count < 0 || ceil_count > fracs.len() as i32 {
            return "-1".to_string();
        }
        let ceil_count = ceil_count as usize;
        fracs.sort_by(|a, b| b.partial_cmp(a).unwrap());
        let error: f64 = fracs[..ceil_count].iter().map(|f| 1.0 - f).sum::<f64>()
            + fracs[ceil_count..].iter().sum::<f64>();
        format!("{:.3}", error)
    }
}
