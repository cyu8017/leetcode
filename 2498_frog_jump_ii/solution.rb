# LeetCode 2498 - Frog Jump II
# https://leetcode.com/problems/frog-jump-ii/

# @param {Integer[]} stones
# @return {Integer}
def max_jump(stones)
  ans = stones[1] - stones[0]
  (2...stones.length).each do |i|
    diff = stones[i] - stones[i - 2]
    ans = diff if diff > ans
  end
  ans
end
