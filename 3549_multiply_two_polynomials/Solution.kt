// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

import kotlin.math.acos
import kotlin.math.cos
import kotlin.math.round
import kotlin.math.sin

class Solution {
    class Complex(var re: Double, var im: Double) {
        fun mul(o: Complex) = Complex(re * o.re - im * o.im, re * o.im + im * o.re)
        fun add(o: Complex) = Complex(re + o.re, im + o.im)
        fun sub(o: Complex) = Complex(re - o.re, im - o.im)
        fun div(x: Double) = Complex(re / x, im / x)
    }

    fun fft(a: Array<Complex>, invert: Boolean) {
        val n = a.size
        var j = 0
        for (i in 1 until n) {
            var bit = n shr 1
            while ((j and bit) != 0) {
                j = j xor bit
                bit = bit shr 1
            }
            j = j xor bit
            if (i < j) {
                val t = a[i]
                a[i] = a[j]
                a[j] = t
            }
        }
        var length = 2
        while (length <= n) {
            val angle = 2 * acos(-1.0) / length * (if (invert) -1 else 1)
            val wlen = Complex(cos(angle), sin(angle))
            var i = 0
            while (i < n) {
                var w = Complex(1.0, 0.0)
                val half = length shr 1
                for (jj in 0 until half) {
                    val u = a[i + jj]
                    val v = a[i + jj + half].mul(w)
                    a[i + jj] = u.add(v)
                    a[i + jj + half] = u.sub(v)
                    w = w.mul(wlen)
                }
                i += length
            }
            length = length shl 1
        }
        if (invert) for (i in 0 until n) a[i] = a[i].div(n.toDouble())
    }

    fun multiply(poly1: IntArray, poly2: IntArray): LongArray {
        if (poly1.isEmpty() || poly2.isEmpty()) return LongArray(0)
        val m = poly1.size + poly2.size - 1
        var n = 1
        while (n < m) n = n shl 1
        val fa = Array(n) { Complex(0.0, 0.0) }
        val fb = Array(n) { Complex(0.0, 0.0) }
        for (i in 0 until n) {
            fa[i] = Complex(if (i < poly1.size) poly1[i].toDouble() else 0.0, 0.0)
            fb[i] = Complex(if (i < poly2.size) poly2[i].toDouble() else 0.0, 0.0)
        }
        fft(fa, false)
        fft(fb, false)
        for (i in 0 until n) fa[i] = fa[i].mul(fb[i])
        fft(fa, true)
        val res = LongArray(m)
        for (i in 0 until m) res[i] = round(fa[i].re).toLong()
        return res
    }
}
