# LeetCode 3999 - Minimum Number of String Groups Through Transformations
# https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

# @param {String[]} words
# @return {Integer}
def minimum_groups(words)
  least_rotation = lambda do |s|
    n = s.length
    i = 0
    j = 1
    k = 0
    while i < n && j < n && k < n
      a = s[(i + k) % n]
      b = s[(j + k) % n]
      if a == b
        k += 1
      else
        if a > b
          i += k + 1
        else
          j += k + 1
        end
        j += 1 if i == j
        k = 0
      end
    end
    i < j ? i : j
  end
  canonical_rotate = lambda do |s|
    n = s.length
    return s if n <= 1
    r = least_rotation.call(s)
    return s if r == 0
    s[r..] + s[0...r]
  end
  keys = words.map do |w|
    even = +""
    odd = +""
    w.length.times do |i|
      if i.even?
        even << w[i]
      else
        odd << w[i]
      end
    end
    canonical_rotate.call(even) + "#" + canonical_rotate.call(odd)
  end
  keys.sort!
  groups = 0
  keys.each_with_index do |key, i|
    groups += 1 if i == 0 || key != keys[i - 1]
  end
  groups
end
