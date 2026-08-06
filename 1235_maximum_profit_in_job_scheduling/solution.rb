# LeetCode 1235 - Maximum Profit in Job Scheduling
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @param {Integer[]} profit
# @return {Integer}
def job_scheduling(start_time, end_time, profit)
  jobs = end_time.zip(start_time, profit).sort_by(&:first)
  ends = [0]
  dp = [0]
  jobs.each do |finish, start, gain|
    i = (ends.bsearch_index { |e| e > start } || ends.length) - 1
    ends << finish
    dp << [dp[-1], dp[i] + gain].max
  end
  dp[-1]
end
