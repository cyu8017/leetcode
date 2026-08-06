# LeetCode 1923 - Longest Common Subpath
# https://leetcode.com/problems/longest-common-subpath/

# @param {Integer} n
# @param {Integer[][]} paths
# @return {Integer}
def longest_common_subpath(n, paths)
  base1 = 911_382_323
  mod1 = 1_000_000_007
  base2 = 972_663_749
  mod2 = 1_000_000_009

  mod_pow = lambda do |base, exp, mod|
    r = 1
    b = base % mod
    e = exp
    while e.positive?
      r = r * b % mod if e.odd?
      b = b * b % mod
      e /= 2
    end
    r
  end

  has_common = lambda do |length|
    return true if length.zero?
    common = nil
    pow1 = mod_pow.call(base1, length, mod1)
    pow2 = mod_pow.call(base2, length, mod2)
    paths.each do |path|
      return false if path.length < length
      h1 = 0
      h2 = 0
      seen = {}
      path.each_with_index do |v, i|
        h1 = (h1 * base1 + (v + 1)) % mod1
        h2 = (h2 * base2 + (v + 1)) % mod2
        if i >= length
          h1 = (h1 - (path[i - length] + 1) * pow1 % mod1 + mod1) % mod1
          h2 = (h2 - (path[i - length] + 1) * pow2 % mod2 + mod2) % mod2
        end
        seen[[h1, h2]] = true if i >= length - 1
      end
      if common.nil?
        common = seen
      else
        common.select! { |k, _| seen[k] }
      end
      return false if common.empty?
    end
    true
  end

  lo = 0
  hi = paths.map(&:length).min
  while lo < hi
    mid = (lo + hi + 1) / 2
    if has_common.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
