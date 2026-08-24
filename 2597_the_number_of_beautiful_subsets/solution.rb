# LeetCode 2597 - The Number of Beautiful Subsets
# https://leetcode.com/problems/the-number-of-beautiful-subsets/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def beautiful_subsets(nums, k)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  groups = {}
  freq.each_key do |key|
    rem = key % k
    groups[rem] ||= []
    groups[rem] << key
  end
  ans = 1
  groups.each_value do |vals|
    vals.sort!
    prev_take = 0
    prev_skip = 1
    prev_val = -10**18
    vals.each do |v|
      ways = 1
      freq[v].times { ways *= 2 }
      ways -= 1
      skip = prev_take + prev_skip
      take = ways * prev_skip
      take += ways * prev_take if prev_val + k != v
      prev_take = take
      prev_skip = skip
      prev_val = v
    end
    ans *= prev_take + prev_skip
  end
  ans - 1
end
