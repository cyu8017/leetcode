
# @param {Integer[]} nums
# @return {Integer}
def array_sign(nums)
  sign = 1
  nums.each do |num|
    return 0 if num == 0
    sign = -sign if num < 0
  end
  sign
end
