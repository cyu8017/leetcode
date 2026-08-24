# LeetCode 0960 - Delete Columns to Make Sorted III
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

# @param {String[]} strs
# @return {Integer}
def min_deletion_size(strs)
  m = strs[0].length
  dp = Array.new(m, 1)
  m.times do |j|
    j.times do |i|
      dp[j] = [dp[j], dp[i] + 1].max if strs.all? { |row| row[i] <= row[j] }
    end
  end
  m - dp.max
end
