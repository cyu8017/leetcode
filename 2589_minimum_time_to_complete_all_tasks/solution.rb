# LeetCode 2589 - Minimum Time to Complete All Tasks
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

# @param {Integer[][]} tasks
# @return {Integer}
def find_minimum_time(tasks)
  tasks = tasks.sort_by { |t| t[1] }
  on = Array.new(2001, false)
  ans = 0
  tasks.each do |start, endi, dur|
    have = 0
    (start..endi).each { |i| have += 1 if on[i] }
    need = dur - have
    i = endi
    while i >= start && need > 0
      unless on[i]
        on[i] = true
        need -= 1
        ans += 1
      end
      i -= 1
    end
  end
  ans
end
