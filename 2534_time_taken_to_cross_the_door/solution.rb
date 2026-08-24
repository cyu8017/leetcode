# LeetCode 2534 - Time Taken to Cross the Door
# https://leetcode.com/problems/time-taken-to-cross-the-door/

# @param {Integer[]} arrival
# @param {Integer[]} state
# @return {Integer[]}
def time_taken(arrival, state)
  n = arrival.length
  ans = Array.new(n, 0)
  enter = []
  exitq = []
  i = 0
  t = 0
  prev = 1
  while i < n || !enter.empty? || !exitq.empty?
    while i < n && arrival[i] <= t
      if state[i] == 0
        enter << i
      else
        exitq << i
      end
      i += 1
    end
    if enter.empty? && exitq.empty?
      if i < n
        t = arrival[i]
        prev = 1
      end
      next
    end
    if prev == 1
      if !exitq.empty?
        ans[exitq.shift] = t
        prev = 1
      else
        ans[enter.shift] = t
        prev = 0
      end
    elsif !enter.empty?
      ans[enter.shift] = t
      prev = 0
    else
      ans[exitq.shift] = t
      prev = 1
    end
    t += 1
  end
  ans
end

alias solve time_taken
