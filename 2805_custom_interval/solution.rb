# LeetCode 2805 - Custom Interval
# https://leetcode.com/problems/custom-interval/

NEXT_ID = [1]
CANCELLED = {}

# @param {Proc} fn
# @param {Integer} delay
# @param {Integer} period
# @return {Integer}
def custom_interval(fn, delay, period)
  NEXT_ID[0] += 1
  interval_id = NEXT_ID[0]
  CANCELLED[interval_id] = false
  interval_id
end

# @param {Integer} interval_id
# @return {NilClass}
def custom_clear_interval(interval_id)
  CANCELLED[interval_id] = true
  nil
end
