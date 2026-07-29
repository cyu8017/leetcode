# LeetCode 1044 - Longest Duplicate Substring
# https://leetcode.com/problems/longest-duplicate-substring/

# @param {String} s
# @return {String}
def longest_dup_substring(s)
  mod = (1 << 61) - 1
  base = 256
  n = s.length
  nums = s.bytes

  search = lambda do |length|
    return 0 if length.zero?

    h = 0
    length.times { |i| h = (h * base + nums[i]) % mod }
    seen = { h => [0] }
    power = base.pow(length, mod)
    (1..(n - length)).each do |i|
      h = (h * base - nums[i - 1] * power + nums[i + length - 1]) % mod
      if seen.key?(h)
        cur = s[i, length]
        seen[h].each do |j|
          return i if s[j, length] == cur
        end
        seen[h] << i
      else
        seen[h] = [i]
      end
    end
    -1
  end

  lo = 0
  hi = n - 1
  start = -1
  best_len = 0
  while lo <= hi
    mid = (lo + hi) / 2
    pos = search.call(mid)
    if pos >= 0
      start = pos
      best_len = mid
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  start >= 0 ? s[start, best_len] : ""
end
