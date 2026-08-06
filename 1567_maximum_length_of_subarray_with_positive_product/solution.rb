# LeetCode 1567 - Maximum Length of Subarray With Positive Product
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

# @param {Integer[]} nums
# @return {Integer}
def get_max_len(nums)
  positive = negative = answer = 0
  nums.each do |x|
    if x == 0
      positive = negative = 0
    elsif x > 0
      positive += 1
      negative = negative.positive? ? negative + 1 : 0
    else
      positive, negative = (negative.positive? ? negative + 1 : 0), positive + 1
    end
    answer = [answer, positive].max
  end
  answer
end
