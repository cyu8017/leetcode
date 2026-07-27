# LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

# @param {String[]} key_name
# @param {String[]} key_time
# @return {String[]}
def alert_names(key_name, key_time)
  times = Hash.new { |h, k| h[k] = [] }
  key_name.zip(key_time).each do |name, t|
    h, m = t.split(":").map(&:to_i)
    times[name] << h * 60 + m
  end
  ans = []
  times.each do |name, a|
    a.sort!
    ans << name if (0...(a.length - 2)).any? { |i| a[i + 2] - a[i] <= 60 }
  end
  ans.sort
end
