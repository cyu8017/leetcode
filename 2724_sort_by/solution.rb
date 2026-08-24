# LeetCode 2724 - Sort By
# https://leetcode.com/problems/sort-by/

# @param {Object[]} arr
# @param {Proc} fn
# @return {Object[]}
def sort_by(arr, fn)
  arr.sort_by { |x| fn.call(x) }
end
