# LeetCode 1122 - Relative Sort Array
# https://leetcode.com/problems/relative-sort-array/

# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer[]}
def relative_sort_array(arr1, arr2)
  count = Hash.new(0)
  arr1.each { |x| count[x] += 1 }
  ans = []
  arr2.each do |x|
    count[x].times { ans << x }
    count.delete(x)
  end
  count.keys.sort.each { |x| count[x].times { ans << x } }
  ans
end
