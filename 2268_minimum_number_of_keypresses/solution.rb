# LeetCode 2268 - Minimum Number of Keypresses
# https://leetcode.com/problems/minimum-number-of-keypresses/

# @param {String} s
# @return {Integer}
def minimum_keypresses(s)
  freq = Array.new(26, 0)
  s.each_char { |c| freq[c.ord - 97] += 1 }
  freq.sort!.reverse!
  ans = 0
  26.times do |i|
    break if freq[i] == 0

    ans += freq[i] * (i / 9 + 1)
  end
  ans
end

alias solve minimum_keypresses
