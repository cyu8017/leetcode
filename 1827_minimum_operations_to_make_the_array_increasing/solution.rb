
# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  ops = 0
  prev = nums[0]
  nums[1..].each do |value|
    if value <= prev
      needed = prev + 1
      ops += needed - value
      prev = needed
    else
      prev = value
    end
  end
  ops
end
