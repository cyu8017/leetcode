# LeetCode 3890 - Integers With Multiple Sum of Two Cubes
# https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

$good3890 = nil

def init3890
  return unless $good3890.nil?
  limit = 1_000_000_000
  cnt = Hash.new(0)
  cubes = Array.new(1001, 0)
  1001.times { |i| cubes[i] = i * i * i }
  (1..1000).each do |a|
    (a..1000).each do |b|
      x = cubes[a] + cubes[b]
      break if x > limit
      cnt[x] += 1
    end
  end
  $good3890 = []
  cnt.each { |k, v| $good3890 << k if v > 1 }
  $good3890.sort!
end

# @param {Integer} n
# @return {Integer[]}
def find_good_integers(n)
  init3890
  lo = 0
  hi = $good3890.length
  while lo < hi
    mid = (lo + hi) / 2
    if $good3890[mid] <= n
      lo = mid + 1
    else
      hi = mid
    end
  end
  $good3890[0, lo]
end
