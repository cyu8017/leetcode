# LeetCode 1313 - Decompress Run Length Encoded List
# https://leetcode.com/problems/decompress-run-length-encoded-list/

def decompress_rl_elist(nums)
  answer = []
  (0...nums.length).step(2) do |i|
    answer.concat(Array.new(nums[i], nums[i + 1]))
  end
  answer
end
