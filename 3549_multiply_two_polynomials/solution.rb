# LeetCode 3549 - Multiply Two Polynomials
# https://leetcode.com/problems/multiply-two-polynomials/

class Complex3549
  attr_accessor :re, :im

  def initialize(re, im)
    @re = re
    @im = im
  end

  def mul(o)
    Complex3549.new(@re * o.re - @im * o.im, @re * o.im + @im * o.re)
  end

  def add(o)
    Complex3549.new(@re + o.re, @im + o.im)
  end

  def sub(o)
    Complex3549.new(@re - o.re, @im - o.im)
  end

  def div(x)
    Complex3549.new(@re / x.to_f, @im / x.to_f)
  end
end

# @param {Integer[]} poly1
# @param {Integer[]} poly2
# @return {Integer[]}
def multiply(poly1, poly2)
  return [] if poly1.empty? || poly2.empty?
  fft = lambda do |a, invert|
    n = a.length
    j = 0
    (1...n).each do |i|
      bit = n >> 1
      while (j & bit) != 0
        j ^= bit
        bit >>= 1
      end
      j ^= bit
      a[i], a[j] = a[j], a[i] if i < j
    end
    length = 2
    while length <= n
      angle = 2 * Math::PI / length * (invert ? -1 : 1)
      wlen = Complex3549.new(Math.cos(angle), Math.sin(angle))
      (0...n).step(length) do |i|
        w = Complex3549.new(1, 0)
        half = length >> 1
        (0...half).each do |jj|
          u = a[i + jj]
          v = a[i + jj + half].mul(w)
          a[i + jj] = u.add(v)
          a[i + jj + half] = u.sub(v)
          w = w.mul(wlen)
        end
      end
      length <<= 1
    end
    (0...n).each { |i| a[i] = a[i].div(n) } if invert
  end
  m = poly1.length + poly2.length - 1
  n = 1
  n <<= 1 while n < m
  fa = Array.new(n) { Complex3549.new(0, 0) }
  fb = Array.new(n) { Complex3549.new(0, 0) }
  (0...n).each do |i|
    fa[i] = Complex3549.new(i < poly1.length ? poly1[i] : 0, 0)
    fb[i] = Complex3549.new(i < poly2.length ? poly2[i] : 0, 0)
  end
  fft.call(fa, false)
  fft.call(fb, false)
  (0...n).each { |i| fa[i] = fa[i].mul(fb[i]) }
  fft.call(fa, true)
  (0...m).map { |i| fa[i].re.round }
end
