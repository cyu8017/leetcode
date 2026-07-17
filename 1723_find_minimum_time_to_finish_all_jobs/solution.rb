# LeetCode 1723 - Find Minimum Time to Finish All Jobs
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

require 'set'

# @param {Integer[]} jobs
# @param {Integer} k
# @return {Integer}
def minimum_time_required(jobs, k)
  jobs = jobs.sort.reverse
  loads = Array.new(k, 0)
  best = jobs.sum

  backtrack = lambda do |i|
    if i == jobs.length
      best = [best, loads.max].min
      next
    end
    seen = Set.new
    k.times do |worker|
      next if seen.include?(loads[worker])
      next if loads[worker] + jobs[i] >= best
      seen << loads[worker]
      loads[worker] += jobs[i]
      backtrack.call(i + 1)
      loads[worker] -= jobs[i]
      break if loads[worker].zero?
    end
  end

  backtrack.call(0)
  best
end
