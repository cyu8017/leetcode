# LeetCode 2323 - Find Minimum Time to Finish All Jobs II
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

# @param {Integer[]} jobs
# @param {Integer[]} workers
# @return {Integer}
def minimum_time(jobs, workers)
  jobs = jobs.sort
  workers = workers.sort
  ans = 0
  jobs.each_index do |i|
    cand = (jobs[i] + workers[i] - 1) / workers[i]
    ans = cand if cand > ans
  end
  ans
end

alias solve minimum_time
