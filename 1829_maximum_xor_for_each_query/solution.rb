
# @param {Integer[]} nums
# @param {Integer} maximum_bit
# @return {Integer[]}
def get_maximum_xor(nums, maximum_bit)
  limit = (1 << maximum_bit) - 1
  current = 0
  nums.each { |num| current ^= num }

  result = []
  (nums.length - 1).downto(0) do |i|
    result << (current ^ limit)
    current ^= nums[i]
  end
  result
end
