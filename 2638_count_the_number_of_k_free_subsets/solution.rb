# LeetCode 2638 - Count the Number of K-Free Subsets
# https://leetcode.com/problems/count-the-number-of-k-free-subsets/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_the_num_of_k_free_subsets(nums, k)
  nums = nums.sort
  groups = {}
  nums.each do |x|
    key = x % k
    groups[key] ||= []
    groups[key] << x
  end
  ans = 1
  groups.each_value do |g|
    prev_val = -1
    prev_take = 0
    prev_skip = 1
    g.each do |v|
      skip = prev_take + prev_skip
      take = prev_val + k == v ? prev_skip : prev_take + prev_skip
      prev_take = take
      prev_skip = skip
      prev_val = v
    end
    ans *= prev_take + prev_skip
  end
  ans
end

def solve(*args)
  count_the_num_of_k_free_subsets(*args)
end
