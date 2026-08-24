# LeetCode 2512 - Reward Top K Students
# https://leetcode.com/problems/reward-top-k-students/

# @param {String[]} positive_feedback
# @param {String[]} negative_feedback
# @param {String[]} report
# @param {Integer[]} student_id
# @param {Integer} k
# @return {Integer[]}
def top_students(positive_feedback, negative_feedback, report, student_id, k)
  pos = {}
  neg = {}
  positive_feedback.each { |w| pos[w] = true }
  negative_feedback.each { |w| neg[w] = true }
  arr = Array.new(report.length)
  report.each_with_index do |r, i|
    score = 0
    r.split(" ").each do |w|
      next if w.empty?

      if pos[w]
        score += 3
      elsif neg[w]
        score -= 1
      end
    end
    arr[i] = [student_id[i], score]
  end
  arr.sort_by! { |x| [-x[1], x[0]] }
  arr[0, k].map { |x| x[0] }
end
