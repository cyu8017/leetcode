# LeetCode 2545 - Sort the Students by Their Kth Score
# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

# @param {Integer[][]} score
# @param {Integer} k
# @return {Integer[][]}
def sort_the_students(score, k)
  score.sort_by { |row| -row[k] }
end
