# LeetCode 1186 - Maximum Subarray Sum with One Deletion
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

# @param {Integer[]} arr
# @return {Integer}
def maximum_sum(arr)
  keep = delete = ans = arr[0]
  arr[1..].each do |x|
    delete = [keep, delete + x].max
    keep = [keep + x, x].max
    ans = [ans, keep, delete].max
  end
  ans
end
