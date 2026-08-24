# LeetCode 3080 - Mark Elements on Array by Performing Queries
# https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def unmarked_sum_array(nums, queries)
  n = nums.length
  s = nums.sum
  mark = Array.new(n, false)
  arr = nums.each_with_index.map { |v, i| [v, i] }
  arr.sort_by! { |a| [a[0], a[1]] }
  ans = Array.new(queries.length, 0)
  j = 0
  queries.each_with_index do |q, qi|
    index = q[0]
    k = q[1]
    unless mark[index]
      mark[index] = true
      s -= nums[index]
    end
    while k > 0 && j < n
      unless mark[arr[j][1]]
        mark[arr[j][1]] = true
        s -= arr[j][0]
        k -= 1
      end
      j += 1
    end
    ans[qi] = s
  end
  ans
end
