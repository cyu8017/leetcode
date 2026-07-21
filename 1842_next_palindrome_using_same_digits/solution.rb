
# @param {String} num
# @return {String}
def next_palindrome(num)
  nums = num.chars
  return '' unless next_permutation_half!(nums)

  n = nums.length
  (n / 2).times { |i| nums[n - i - 1] = nums[i] }
  nums.join
end

def next_permutation_half!(nums)
  n = nums.length / 2
  i = n - 2
  i -= 1 while i >= 0 && nums[i] >= nums[i + 1]
  return false if i < 0

  j = n - 1
  j -= 1 while nums[j] <= nums[i]
  nums[i], nums[j] = nums[j], nums[i]
  nums[(i + 1)...n] = nums[(i + 1)...n].reverse
  true
end
