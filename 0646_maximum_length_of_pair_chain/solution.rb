# LeetCode 0646 - Maximum Length of Pair Chain
# https://leetcode.com/problems/maximum-length-of-pair-chain/

# @param {Integer[][]} pairs
# @return {Integer}
def find_longest_chain(pairs)
  pairs = pairs.sort_by { |pair| pair[1] }
  length = 0
  current_end = -Float::INFINITY
  pairs.each do |left, right|
    if left > current_end
      length += 1
      current_end = right
    end
  end
  length
end
