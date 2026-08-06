# LeetCode 1331 - Rank Transform Of An Array
# https://leetcode.com/problems/rank-transform-of-an-array/

def array_rank_transform(arr)
  rank = {}
  arr.uniq.sort.each_with_index { |value, i| rank[value] = i + 1 }
  arr.map { |value| rank[value] }
end
