# LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

# @param {Integer[]} tasks
# @param {Integer} session_time
# @return {Integer}
def min_sessions(tasks, session_time)
  n = tasks.length
  inf = [n + 1, 0]
  dp = Array.new(1 << n, inf)
  dp[0] = [1, 0]
  (1 << n).times do |mask|
    sessions, used = dp[mask]
    next if sessions > n
    n.times do |i|
      next unless (mask & (1 << i)).zero?
      t = tasks[i]
      nmask = mask | (1 << i)
      cand = if used + t <= session_time
               [sessions, used + t]
             else
               [sessions + 1, t]
             end
      dp[nmask] = cand if cand < dp[nmask]
    end
  end
  dp[(1 << n) - 1][0]
end
