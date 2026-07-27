# LeetCode 1629 - Slowest Key
# https://leetcode.com/problems/slowest-key/

# @param {Integer[]} release_times
# @param {String} keys_pressed
# @return {Character}
def slowest_key(release_times, keys_pressed)
  best_duration = release_times[0]
  best_key = keys_pressed[0]
  (1...release_times.length).each do |i|
    duration = release_times[i] - release_times[i - 1]
    if duration > best_duration || (duration == best_duration && keys_pressed[i] > best_key)
      best_duration = duration
      best_key = keys_pressed[i]
    end
  end
  best_key
end
