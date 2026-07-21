
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_frequency(nums, k)
  nums = nums.sort
  left = 0
  window_sum = 0
  best = 0

  nums.each_with_index do |value, right|
    window_sum += value
    while value * (right - left + 1) - window_sum > k
      window_sum -= nums[left]
      left += 1
    end
    best = [best, right - left + 1].max
  end
  best
end
