# LeetCode 1470 - Shuffle The Array
# https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums, n)
  nums[0, n].zip(nums[n..]).flatten
end
