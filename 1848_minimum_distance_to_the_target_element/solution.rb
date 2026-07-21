
# @param {Integer[]} nums
# @param {Integer} target
# @param {Integer} start
# @return {Integer}
def get_min_distance(nums, target, start)
  best = nums.length
  nums.each_with_index do |value, i|
    best = [best, (i - start).abs].min if value == target
  end
  best
end
