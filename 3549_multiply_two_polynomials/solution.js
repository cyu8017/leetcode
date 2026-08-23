// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

function Complex(re, im) { this.re = re; this.im = im; }
Complex.prototype.mul = function(o) { return new Complex(this.re * o.re - this.im * o.im, this.re * o.im + this.im * o.re); };
Complex.prototype.add = function(o) { return new Complex(this.re + o.re, this.im + o.im); };
Complex.prototype.sub = function(o) { return new Complex(this.re - o.re, this.im - o.im); };
Complex.prototype.div = function(x) { return new Complex(this.re / x, this.im / x); };
function fft(a, invert) {
    const n = a.length;
    for (let i = 1, j = 0; i < n; i++) {
        let bit = n >> 1;
        for (; (j & bit) !== 0; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) { const t = a[i]; a[i] = a[j]; a[j] = t; }
    }
    for (let length = 2; length <= n; length <<= 1) {
        const angle = 2 * Math.PI / length * (invert ? -1 : 1);
        const wlen = new Complex(Math.cos(angle), Math.sin(angle));
        for (let i = 0; i < n; i += length) {
            let w = new Complex(1, 0);
            const half = length >> 1;
            for (let j = 0; j < half; j++) {
                const u = a[i + j];
                const v = a[i + j + half].mul(w);
                a[i + j] = u.add(v);
                a[i + j + half] = u.sub(v);
                w = w.mul(wlen);
            }
        }
    }
    if (invert) for (let i = 0; i < n; i++) a[i] = a[i].div(n);
}
var multiply = function(poly1, poly2) {
    if (poly1.length === 0 || poly2.length === 0) return [];
    const m = poly1.length + poly2.length - 1;
    let n = 1;
    while (n < m) n <<= 1;
    const fa = new Array(n), fb = new Array(n);
    for (let i = 0; i < n; i++) {
        fa[i] = new Complex(i < poly1.length ? poly1[i] : 0, 0);
        fb[i] = new Complex(i < poly2.length ? poly2[i] : 0, 0);
    }
    fft(fa, false);
    fft(fb, false);
    for (let i = 0; i < n; i++) fa[i] = fa[i].mul(fb[i]);
    fft(fa, true);
    const res = new Array(m);
    for (let i = 0; i < m; i++) res[i] = Math.round(fa[i].re);
    return res;
};
