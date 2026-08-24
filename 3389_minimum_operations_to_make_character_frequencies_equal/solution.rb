# LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
# https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

# @param {String} s
# @return {Integer}
def make_string_good(s)
  freq = Array.new(26, 0)
  s.each_char { |c| freq[c.ord - 97] += 1 }
  ans = s.length
  (1..s.length).each do |t|
    pool = 0
    26.times { |i| pool += freq[i] - t if freq[i] > t }
    deficit = 0
    26.times { |i| deficit += t - freq[i] if freq[i] < t }
    ops = [pool, deficit].max
    ans = ops if ops < ans
  end
  ans = s.length if s.length < ans
  ans
end
