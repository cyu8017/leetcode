// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

class Solution {
    struct Complex {
        var re: Double
        var im: Double
        func mul(_ o: Complex) -> Complex { Complex(re: re * o.re - im * o.im, im: re * o.im + im * o.re) }
        func add(_ o: Complex) -> Complex { Complex(re: re + o.re, im: im + o.im) }
        func sub(_ o: Complex) -> Complex { Complex(re: re - o.re, im: im - o.im) }
        func div(_ x: Double) -> Complex { Complex(re: re / x, im: im / x) }
    }

    func fft(_ a: inout [Complex], _ invert: Bool) {
        let n = a.count
        var j = 0
        if n > 1 {
            for i in 1..<n {
                var bit = n >> 1
                while (j & bit) != 0 { j ^= bit; bit >>= 1 }
                j ^= bit
                if i < j { a.swapAt(i, j) }
            }
        }
        var length = 2
        while length <= n {
            let angle = 2 * Double.pi / Double(length) * (invert ? -1 : 1)
            let wlen = Complex(re: cos(angle), im: sin(angle))
            var i = 0
            while i < n {
                var w = Complex(re: 1, im: 0)
                let half = length >> 1
                for jj in 0..<half {
                    let u = a[i + jj]
                    let v = a[i + jj + half].mul(w)
                    a[i + jj] = u.add(v)
                    a[i + jj + half] = u.sub(v)
                    w = w.mul(wlen)
                }
                i += length
            }
            length <<= 1
        }
        if invert {
            for i in 0..<n { a[i] = a[i].div(Double(n)) }
        }
    }

    func multiply(_ poly1: [Int], _ poly2: [Int]) -> [Int] {
        if poly1.isEmpty || poly2.isEmpty { return [] }
        let m = poly1.count + poly2.count - 1
        var n = 1
        while n < m { n <<= 1 }
        var fa = Array(repeating: Complex(re: 0, im: 0), count: n)
        var fb = Array(repeating: Complex(re: 0, im: 0), count: n)
        for i in 0..<n {
            fa[i] = Complex(re: i < poly1.count ? Double(poly1[i]) : 0, im: 0)
            fb[i] = Complex(re: i < poly2.count ? Double(poly2[i]) : 0, im: 0)
        }
        fft(&fa, false)
        fft(&fb, false)
        for i in 0..<n { fa[i] = fa[i].mul(fb[i]) }
        fft(&fa, true)
        var res = Array(repeating: 0, count: m)
        for i in 0..<m { res[i] = Int(fa[i].re.rounded()) }
        return res
    }
}
