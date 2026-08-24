// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

impl Solution {
    fn fft(a: &mut [(f64, f64)], invert: bool) {
        let n = a.len();
        let mut j = 0;
        for i in 1..n {
            let mut bit = n >> 1;
            while j & bit != 0 {
                j ^= bit;
                bit >>= 1;
            }
            j ^= bit;
            if i < j {
                a.swap(i, j);
            }
        }
        let mut length = 2;
        while length <= n {
            let angle = 2.0 * std::f64::consts::PI / length as f64 * if invert { -1.0 } else { 1.0 };
            let wlen = (angle.cos(), angle.sin());
            for i in (0..n).step_by(length) {
                let mut w = (1.0, 0.0);
                let half = length >> 1;
                for jj in 0..half {
                    let u = a[i + jj];
                    let v = (a[i + jj + half].0 * w.0 - a[i + jj + half].1 * w.1, a[i + jj + half].0 * w.1 + a[i + jj + half].1 * w.0);
                    a[i + jj] = (u.0 + v.0, u.1 + v.1);
                    a[i + jj + half] = (u.0 - v.0, u.1 - v.1);
                    w = (w.0 * wlen.0 - w.1 * wlen.1, w.0 * wlen.1 + w.1 * wlen.0);
                }
            }
            length <<= 1;
        }
        if invert {
            for x in a.iter_mut() {
                x.0 /= n as f64;
                x.1 /= n as f64;
            }
        }
    }

    pub fn multiply(poly1: Vec<i32>, poly2: Vec<i32>) -> Vec<i64> {
        if poly1.is_empty() || poly2.is_empty() {
            return vec![];
        }
        let m = poly1.len() + poly2.len() - 1;
        let mut n = 1;
        while n < m {
            n <<= 1;
        }
        let mut fa = vec![(0.0, 0.0); n];
        let mut fb = vec![(0.0, 0.0); n];
        for i in 0..poly1.len() {
            fa[i] = (poly1[i] as f64, 0.0);
        }
        for i in 0..poly2.len() {
            fb[i] = (poly2[i] as f64, 0.0);
        }
        Self::fft(&mut fa, false);
        Self::fft(&mut fb, false);
        for i in 0..n {
            fa[i] = (fa[i].0 * fb[i].0 - fa[i].1 * fb[i].1, fa[i].0 * fb[i].1 + fa[i].1 * fb[i].0);
        }
        Self::fft(&mut fa, true);
        (0..m).map(|i| fa[i].0.round() as i64).collect()
    }
}
