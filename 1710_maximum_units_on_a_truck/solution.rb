# LeetCode 1710 - Maximum Units on a Truck
# https://leetcode.com/problems/maximum-units-on-a-truck/

# @param {Integer[][]} box_types
# @param {Integer} truck_size
# @return {Integer}
def maximum_units(box_types, truck_size)
  total = 0
  box_types.sort_by { |item| -item[1] }.each do |count, units|
    take = [count, truck_size].min
    total += take * units
    truck_size -= take
    break if truck_size.zero?
  end
  total
end
