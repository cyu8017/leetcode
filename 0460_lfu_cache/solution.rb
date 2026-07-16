# LeetCode 0460 - LFU Cache
# https://leetcode.com/problems/lfu-cache/

class LFUCache
  def initialize(capacity)
    @capacity = capacity
    @min_freq = 0
    @key_values = {}
    @key_freqs = {}
    @freq_keys = Hash.new { |hash, key| hash[key] = [] }
  end

  def get(key)
    return -1 unless @key_values.key?(key)

    touch(key)
    @key_values[key]
  end

  def put(key, value)
    return if @capacity == 0

    if @key_values.key?(key)
      @key_values[key] = value
      touch(key)
      return
    end

    if @key_values.length >= @capacity
      evict = @freq_keys[@min_freq].shift
      @key_values.delete(evict)
      @key_freqs.delete(evict)
    end

    @key_values[key] = value
    @key_freqs[key] = 1
    @freq_keys[1] << key
    @min_freq = 1
  end

  private

  def touch(key)
    freq = @key_freqs[key]
    bucket = @freq_keys[freq]
    bucket.delete(key)
    @min_freq += 1 if bucket.empty? && freq == @min_freq
    @key_freqs[key] = freq + 1
    @freq_keys[freq + 1] << key
  end
end
