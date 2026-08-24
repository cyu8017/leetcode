# LeetCode 3683 - Earliest Time to Finish One Task
# https://leetcode.com/problems/earliest-time-to-finish-one-task/

# @param {Integer[][]} tasks
# @return {Integer}
def earliest_time(tasks)
  ans = 200
  tasks.each { |task| ans = [ans, task[0] + task[1]].min }
  ans
end
