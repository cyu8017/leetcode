# LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
# https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

# @param {Integer} k
# @param {Integer} x
# @return {Integer}
def find_maximum_number(k, x)
  l = 1
  r = 10**17
  while l < r
    mid = (l + r + 1) >> 1
    if price_sum(mid, x) <= k
      l = mid
    else
      r = mid - 1
    end
  end
  l
end

def price_sum(num, x)
  m = 0
  t = num
  while t > 0
    m += 1
    t >>= 1
  end
  f = Array.new(65) { Array.new(65, -1) }
  dfs = lambda do |pos, cnt, limit|
    return cnt if pos == 0
    return f[pos][cnt] if !limit && f[pos][cnt] != -1

    ans = 0
    up = limit ? ((num >> (pos - 1)) & 1) : 1
    (0..up).each do |i|
      v = cnt
      v += 1 if i == 1 && pos % x == 0
      ans += dfs.call(pos - 1, v, limit && i == up)
    end
    f[pos][cnt] = ans unless limit
    ans
  end
  dfs.call(m, 0, true)
end
