# LeetCode 1947 - Maximum Compatibility Score Sum
# https://leetcode.com/problems/maximum-compatibility-score-sum/

# @param {Integer[][]} students
# @param {Integer[][]} mentors
# @return {Integer}
def max_compatibility_sum(students, mentors)
  m = students.length
  score = Array.new(m) { Array.new(m, 0) }
  m.times do |i|
    m.times do |j|
      score[i][j] = students[i].zip(mentors[j]).count { |a, b| a == b }
    end
  end
  memo = {}
  dp = lambda do |i, mask|
    return 0 if i == m
    key = [i, mask]
    return memo[key] if memo.key?(key)
    best = 0
    m.times do |j|
      next unless (mask & (1 << j)).zero?
      best = [best, score[i][j] + dp.call(i + 1, mask | (1 << j))].max
    end
    memo[key] = best
  end
  dp.call(0, 0)
end
