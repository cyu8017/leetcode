# LeetCode 0621 - Task Scheduler
# https://leetcode.com/problems/task-scheduler/

# @param {Character[]} tasks
# @param {Integer} n
# @return {Integer}
def least_interval(tasks, n)
  counts = Hash.new(0)
  tasks.each { |task| counts[task] += 1 }
  max_freq = counts.values.max
  max_count = counts.values.count { |value| value == max_freq }
  [tasks.length, (max_freq - 1) * (n + 1) + max_count].max
end
