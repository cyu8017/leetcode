# LeetCode 4012 - Count of Unfinished Tasks After Each Shift
# https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

# @param {Integer[]} tasks
# @param {Integer[]} shifts
# @return {Integer[]}
def count_tasks(tasks, shifts)
  m = tasks.length
  n = shifts.length
  s = Array.new(m + 1, 0)
  m.times { |i| s[i + 1] = s[i] + tasks[i] }
  ans = Array.new(n, 0)
  i_idx = 0
  cur = 0
  n.times do |j|
    if shifts[j] < tasks[i_idx] - cur
      cur += shifts[j]
      ans[j] = m - i_idx
    else
      t = shifts[j] - (tasks[i_idx] - cur)
      if t >= s[m] - s[i_idx + 1]
        i_idx = 0
        cur = 0
      else
        l = i_idx + 1
        r = m
        while l < r
          mid = (l + r) >> 1
          if t < s[mid + 1] - s[i_idx + 1]
            r = mid
          else
            l = mid + 1
          end
        end
        cur = t - (s[l] - s[i_idx + 1])
        i_idx = l
        ans[j] = m - i_idx
      end
    end
  end
  ans
end
