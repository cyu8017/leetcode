# LeetCode 0636 - Exclusive Time of Functions
# https://leetcode.com/problems/exclusive-time-of-functions/

# @param {Integer} n
# @param {String[]} logs
# @return {Integer[]}
def exclusive_time(n, logs)
  result = Array.new(n, 0)
  stack = []
  prev_time = 0

  logs.each do |log|
    func_id_str, event, time_str = log.split(":")
    func_id = func_id_str.to_i
    time = time_str.to_i

    if event == "start"
      result[stack[-1]] += time - prev_time unless stack.empty?
      stack << func_id
      prev_time = time
    else
      result[stack.pop] += time - prev_time + 1
      prev_time = time + 1
    end
  end

  result
end
