# LeetCode 2622 - Cache With Time Limit
# https://leetcode.com/problems/cache-with-time-limit/

class TimeLimitedCache
  def initialize
    @data = {}
  end

  def set(key, value, duration)
    now = (Time.now.to_f * 1000).to_i
    e = @data[key]
    alive = !e.nil? && e[:expire] > now
    @data[key] = { value: value, expire: now + duration }
    alive
  end

  def get(key)
    now = (Time.now.to_f * 1000).to_i
    e = @data[key]
    return -1 if e.nil? || e[:expire] <= now

    e[:value]
  end

  def count
    now = (Time.now.to_f * 1000).to_i
    cnt = 0
    dead = []
    @data.each do |k, e|
      if e[:expire] > now
        cnt += 1
      else
        dead << k
      end
    end
    dead.each { |k| @data.delete(k) }
    cnt
  end
end

# @param {Object} actions
# @return {TimeLimitedCache}
def time_limited_cache(_actions = nil)
  TimeLimitedCache.new
end
