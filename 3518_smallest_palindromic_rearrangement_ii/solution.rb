# LeetCode 3518 - Smallest Palindromic Rearrangement II
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

# @param {String} s
# @param {Integer} k
# @return {String}
def smallest_palindrome(s, k)
  maxv = 1000001
  nck = lambda do |n, kk|
    return 0 if kk < 0 || kk > n
    res = 1
    kk = n - kk if kk > n - kk
    (1..kk).each do |i|
      res = res * (n - i + 1) / i
      return maxv if res >= maxv
    end
    res
  end
  count_arr = lambda do |h|
    total = 0
    h.each { |f| total += f }
    res = 1
    h.each do |f|
      res *= nck.call(total, f)
      return maxv if res >= maxv
      total -= f
    end
    res
  end
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  odd = 0
  cnt.each { |c| odd += 1 if c.odd? }
  return "" if odd > 1
  half = Array.new(26, 0)
  mid = ""
  (0...26).each do |i|
    half[i] = cnt[i] / 2
    mid = (97 + i).chr if cnt[i].odd?
  end
  return "" if count_arr.call(half) < k
  half_len = 0
  half.each { |f| half_len += f }
  left = ""
  half_len.times do
    (0...26).each do |i|
      next if half[i] == 0
      half[i] -= 1
      arr = count_arr.call(half)
      if arr >= k
        left += (97 + i).chr
        break
      end
      k -= arr
      half[i] += 1
    end
  end
  res = left
  res += mid unless mid.empty?
  (left.length - 1).downto(0) { |i| res += left[i] }
  res
end
