# LeetCode 3199 - Count Triplets with Even XOR Set Bits I
# https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

# @param {Integer[]} a
# @param {Integer[]} b
# @param {Integer[]} c
# @return {Integer}
def triplet_count(a, b, c)
  bit_count = lambda do |x|
    n = 0
    while x > 0
      n += x & 1
      x >>= 1
    end
    n
  end
  cnt1 = [0, 0]
  cnt2 = [0, 0]
  cnt3 = [0, 0]
  a.each { |x| cnt1[bit_count.call(x) % 2] += 1 }
  b.each { |x| cnt2[bit_count.call(x) % 2] += 1 }
  c.each { |x| cnt3[bit_count.call(x) % 2] += 1 }
  ans = 0
  (0...2).each do |i|
    (0...2).each do |j|
      (0...2).each do |k|
        ans += cnt1[i] * cnt2[j] * cnt3[k] if (i + j + k).even?
      end
    end
  end
  ans
end
