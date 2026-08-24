# LeetCode 2624 - Snail Traversal
# https://leetcode.com/problems/snail-traversal/

# @param {Integer[]} nums
# @param {Integer} rows_count
# @param {Integer} cols_count
# @return {Integer[][]}
def snail(nums, rows_count, cols_count)
  return [] if rows_count * cols_count != nums.length

  ans = Array.new(rows_count) { Array.new(cols_count, 0) }
  idx = 0
  (0...cols_count).each do |c|
    if c.even?
      (0...rows_count).each do |r|
        ans[r][c] = nums[idx]
        idx += 1
      end
    else
      (rows_count - 1).downto(0) do |r|
        ans[r][c] = nums[idx]
        idx += 1
      end
    end
  end
  ans
end

def solve(*args)
  snail(*args)
end
