# LeetCode 0944 - Delete Columns to Make Sorted
# https://leetcode.com/problems/delete-columns-to-make-sorted/

# @param {String[]} strs
# @return {Integer}
def min_deletion_size(strs)
  (0...strs[0].length).count do |c|
    (0...(strs.length - 1)).any? { |r| strs[r][c] > strs[r + 1][c] }
  end
end
