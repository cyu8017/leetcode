# LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
# https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

# @param {String[]} words
# @return {Integer[]}
def longest_common_prefix(words)
  n = words.length
  tm = {}
  keys = []
  calc = lambda do |s, t|
    m = [s.length, t.length].min
    (0...m).each { |k| return k if s[k] != t[k] }
    m
  end
  add_key = lambda do |x|
    unless tm.key?(x)
      tm[x] = 0
      lo = 0
      hi = keys.length
      while lo < hi
        mid = (lo + hi) >> 1
        if keys[mid] < x
          lo = mid + 1
        else
          hi = mid
        end
      end
      keys.insert(lo, x)
    end
    tm[x] += 1
  end
  rem_key = lambda do |x|
    c = tm[x] - 1
    if c == 0
      tm.delete(x)
      ix = keys.index(x)
      keys.delete_at(ix) if ix
    else
      tm[x] = c
    end
  end
  add = lambda do |i, j|
    add_key.call(calc.call(words[i], words[j])) if i >= 0 && i < n && j >= 0 && j < n
  end
  remove = lambda do |i, j|
    rem_key.call(calc.call(words[i], words[j])) if i >= 0 && i < n && j >= 0 && j < n
  end
  (0...(n - 1)).each { |i| add.call(i, i + 1) }
  ans = Array.new(n, 0)
  (0...n).each do |i|
    remove.call(i, i + 1)
    remove.call(i - 1, i)
    add.call(i - 1, i + 1)
    ans[i] = keys[-1] if !keys.empty? && keys[-1] > 0
    remove.call(i - 1, i + 1)
    add.call(i - 1, i)
    add.call(i, i + 1)
  end
  ans
end
