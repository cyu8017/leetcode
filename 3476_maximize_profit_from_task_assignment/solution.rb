# LeetCode 3476 - Maximize Profit from Task Assignment
# https://leetcode.com/problems/maximize-profit-from-task-assignment/

# @param {Integer[]} workers
# @param {Integer[][]} tasks
# @return {Integer}
def max_profit(workers, tasks)
  workers = workers.sort
  tasks = tasks.sort_by { |t| t[0] }
  ans = 0
  used = Array.new(tasks.length, false)
  workers.each do |w|
    best = -1
    bi = -1
    (0...tasks.length).each do |i|
      next if used[i]
      break if tasks[i][0] > w

      if tasks[i][1] > best
        best = tasks[i][1]
        bi = i
      end
    end
    if bi >= 0
      used[bi] = true
      ans += best
    end
  end
  ans
end
