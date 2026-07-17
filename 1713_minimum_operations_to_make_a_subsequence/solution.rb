# LeetCode 1713 - Minimum Operations to Make a Subsequence
# https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

# @param {Integer[]} target
# @param {Integer[]} arr
# @return {Integer}
def min_operations(target, arr)
  pos = {}
  target.each_with_index { |value, i| pos[value] = i }
  lis = []
  arr.each do |value|
    idx = pos[value]
    next if idx.nil?
    place = lis.bsearch_index { |x| x >= idx }
    if place.nil?
      lis << idx
    else
      lis[place] = idx
    end
  end
  target.length - lis.length
end
