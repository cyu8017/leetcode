# LeetCode 2365 - Task Scheduler II
# https://leetcode.com/problems/task-scheduler-ii/

# @param {Integer[]} tasks
# @param {Integer} space
# @return {Integer}
def task_scheduler_ii(tasks, space)
  nxt = {}
  day = 0
  tasks.each do |t|
    day = nxt[t] if nxt.key?(t) && nxt[t] > day
    day += 1
    nxt[t] = day + space
  end
  day
end
