# LeetCode 3839 - Number of Prefix Connected Groups
# https://leetcode.com/problems/number-of-prefix-connected-groups/

# @param {String[]} words
# @param {Integer} k
# @return {Integer}
def prefix_connected(words, k)
  cnt = Hash.new(0)
  words.each do |w|
    cnt[w[0, k]] += 1 if w.length >= k
  end
  ans = 0
  cnt.each_value { |v| ans += 1 if v > 1 }
  ans
end
