# LeetCode 0955 - Delete Columns to Make Sorted II
# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

# @param {String[]} strs
# @return {Integer}
def min_deletion_size(strs)
  n = strs.length
  m = strs[0].length
  sorted_pair = Array.new(n - 1, false)
  deleted = 0
  m.times do |c|
    if (0...(n - 1)).any? { |r| !sorted_pair[r] && strs[r][c] > strs[r + 1][c] }
      deleted += 1
      next
    end
    (0...(n - 1)).each do |r|
      sorted_pair[r] = true if strs[r][c] < strs[r + 1][c]
    end
  end
  deleted
end
