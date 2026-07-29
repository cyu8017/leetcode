# LeetCode 1086 - High Five
# https://leetcode.com/problems/high-five/

# @param {Integer[][]} items
# @return {Integer[][]}
def high_five(items)
  scores = Hash.new { |h, k| h[k] = [] }
  items.each do |student_id, score|
    scores[student_id] << score
  end
  scores.keys.sort.map do |student_id|
    top = scores[student_id].sort.reverse.take(5)
    [student_id, top.sum / 5]
  end
end
