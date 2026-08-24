# LeetCode 0639 - Decode Ways II
# https://leetcode.com/problems/decode-ways-ii/

# @param {String} s
# @return {Integer}
def num_decodings(s)
  mod = 10**9 + 7

  one = lambda do |ch|
    return 9 if ch == "*"
    return 0 if ch == "0"

    1
  end

  two = lambda do |a, b|
    return 15 if a == "*" && b == "*"
    return b <= "6" ? 2 : 1 if a == "*"
    if b == "*"
      return 9 if a == "1"
      return 6 if a == "2"

      return 0
    end
    value = a.to_i * 10 + b.to_i
    (10..26).cover?(value) ? 1 : 0
  end

  prev2 = 1
  prev1 = one.call(s[0])
  (1...s.length).each do |i|
    cur = (one.call(s[i]) * prev1 + two.call(s[i - 1], s[i]) * prev2) % mod
    prev2 = prev1
    prev1 = cur
  end
  prev1
end
