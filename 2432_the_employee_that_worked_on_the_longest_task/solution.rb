# LeetCode 2432 - The Employee That Worked on the Longest Task
# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

# @param {Integer} n
# @param {Integer[][]} logs
# @return {Integer}
def hardest_worker(n, logs)
  ans = logs[0][0]
  best = logs[0][1]
  prev = 0
  logs.each do |emp, t|
    dur = t - prev
    if dur > best || (dur == best && emp < ans)
      best = dur
      ans = emp
    end
    prev = t
  end
  ans
end
