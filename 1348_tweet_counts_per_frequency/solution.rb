# LeetCode 1348 - Tweet Counts Per Frequency
# https://leetcode.com/problems/tweet-counts-per-frequency/

class TweetCounts
  def initialize
    @times = Hash.new { |h, k| h[k] = [] }
  end

  def record_tweet(tweet_name, time)
    arr = @times[tweet_name]
    idx = arr.bsearch_index { |x| x >= time } || arr.length
    arr.insert(idx, time)
  end

  def get_tweet_counts_per_frequency(freq, tweet_name, start_time, end_time)
    size = { 'minute' => 60, 'hour' => 3600, 'day' => 86400 }[freq]
    times = @times[tweet_name]
    answer = []
    start = start_time
    while start <= end_time
      ending = [end_time, start + size - 1].min
      left = times.bsearch_index { |x| x >= start } || times.length
      right = times.bsearch_index { |x| x > ending } || times.length
      answer << (right - left)
      start += size
    end
    answer
  end
end
