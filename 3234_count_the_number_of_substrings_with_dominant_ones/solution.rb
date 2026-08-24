# LeetCode 3234 - Count the Number of Substrings With Dominant Ones
# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

# @param {String} s
# @return {Integer}
def number_of_substrings(s)
  n = s.length
  nxt = Array.new(n + 1, 0)
  nxt[n] = n
  (n - 1).downto(0) do |i|
    nxt[i] = nxt[i + 1]
    nxt[i] = i if s[i] == "0"
  end
  ans = 0
  (0...n).each do |i|
    cnt0 = s[i] == "0" ? 1 : 0
    j = i
    while j < n && cnt0 * cnt0 <= n
      cnt1 = nxt[j + 1] - i - cnt0
      ans += [nxt[j + 1] - j, cnt1 - cnt0 * cnt0 + 1].min if cnt1 >= cnt0 * cnt0
      j = nxt[j + 1]
      cnt0 += 1
    end
  end
  ans
end
