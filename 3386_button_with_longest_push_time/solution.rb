# LeetCode 3386 - Button with Longest Push Time
# https://leetcode.com/problems/button-with-longest-push-time/

# @param {Integer[][]} events
# @return {Integer}
def button_with_longest_time(events)
  best_t = events[0][1]
  best_i = events[0][0]
  (1...events.length).each do |i|
    t = events[i][1] - events[i - 1][1]
    if t > best_t || (t == best_t && events[i][0] < best_i)
      best_t = t
      best_i = events[i][0]
    end
  end
  best_i
end
