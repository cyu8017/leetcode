# LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_difference(s, k)
  n = s.length
  ans = -10**9
  (0...5).each do |a|
    (0...5).each do |b|
      next if a == b

      pref_a = Array.new(n + 1, 0)
      pref_b = Array.new(n + 1, 0)
      (0...n).each do |i|
        pref_a[i + 1] = pref_a[i]
        pref_b[i + 1] = pref_b[i]
        pref_a[i + 1] += 1 if s[i].ord - 48 == a
        pref_b[i + 1] += 1 if s[i].ord - 48 == b
      end
      (0...n).each do |i|
        ((i + k - 1)...n).each do |j|
          fa = pref_a[j + 1] - pref_a[i]
          fb = pref_b[j + 1] - pref_b[i]
          ans = fa - fb if fa.odd? && fb.even? && fb > 0 && fa - fb > ans
        end
      end
    end
  end
  ans
end
