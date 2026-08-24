# LeetCode 2067 - Number of Equal Count Substrings
# https://leetcode.com/problems/number-of-equal-count-substrings/

# @param {String} s
# @param {Integer} count
# @return {Integer}
def equal_count_substrings(s, count)
  ans = 0
  n = s.length
  seen = Array.new(26, false)
  max_unique = 0
  s.each_char do |c|
    i = c.ord - 97
    unless seen[i]
      seen[i] = true
      max_unique += 1
    end
  end
  (1..max_unique).each do |u|
    need_len = u * count
    break if need_len > n

    freq = Array.new(26, 0)
    have = 0
    n.times do |i|
      c = s[i].ord - 97
      freq[c] += 1
      if freq[c] == count
        have += 1
      elsif freq[c] == count + 1
        have -= 1
      end
      if i >= need_len
        p = s[i - need_len].ord - 97
        if freq[p] == count
          have -= 1
        elsif freq[p] == count + 1
          have += 1
        end
        freq[p] -= 1
      end
      ans += 1 if i + 1 >= need_len && have == u
    end
  end
  ans
end

alias solve equal_count_substrings
