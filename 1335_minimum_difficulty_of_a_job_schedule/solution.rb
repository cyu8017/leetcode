# LeetCode 1335 - Minimum Difficulty Of A Job Schedule
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

def min_difficulty(job_difficulty, d)
  n = job_difficulty.length
  return -1 if n < d
  dp = Array.new(n, 10**9)
  hardest = 0
  job_difficulty.each_with_index do |value, i|
    hardest = [hardest, value].max
    dp[i] = hardest
  end
  (1...d).each do |_day|
    nxt = Array.new(n, 10**9)
    (_day...n).each do |ending|
      hardest = 0
      ending.downto(_day) do |start|
        hardest = [hardest, job_difficulty[start]].max
        nxt[ending] = [nxt[ending], dp[start - 1] + hardest].min
      end
    end
    dp = nxt
  end
  dp[-1]
end
