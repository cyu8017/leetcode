# LeetCode 3861 - Minimum Capacity Box
# https://leetcode.com/problems/minimum-capacity-box/

# @param {Integer[]} capacity
# @param {Integer} item_size
# @return {Integer}
def minimum_index(capacity, item_size)
  ans = -1
  capacity.each_with_index do |c, i|
    ans = i if c >= item_size && (ans == -1 || c < capacity[ans])
  end
  ans
end
