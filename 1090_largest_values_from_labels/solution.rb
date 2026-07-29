# LeetCode 1090 - Largest Values From Labels
# https://leetcode.com/problems/largest-values-from-labels/

# @param {Integer[]} values
# @param {Integer[]} labels
# @param {Integer} num_wanted
# @param {Integer} use_limit
# @return {Integer}
def largest_vals_from_labels(values, labels, num_wanted, use_limit)
  items = values.zip(labels).sort_by { |v, _| -v }
  used = Hash.new(0)
  ans = 0
  taken = 0
  items.each do |value, label|
    break if taken == num_wanted

    next unless used[label] < use_limit

    used[label] += 1
    ans += value
    taken += 1
  end
  ans
end
