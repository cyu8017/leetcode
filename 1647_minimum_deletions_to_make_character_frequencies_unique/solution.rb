# LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

# @param {String} s
# @return {Integer}
def min_deletions(s)
  count = Hash.new(0)
  s.each_char { |ch| count[ch] += 1 }
  used = {}
  ans = 0
  count.values.each do |x|
    while x.positive? && used[x]
      x -= 1
      ans += 1
    end
    used[x] = true
  end
  ans
end
