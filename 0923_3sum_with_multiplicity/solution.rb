# LeetCode 0923 - 3Sum With Multiplicity
# https://leetcode.com/problems/3sum-with-multiplicity/

# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def three_sum_multi(arr, target)
  mod = 10**9 + 7
  count = Hash.new(0)
  arr.each { |x| count[x] += 1 }
  keys = count.keys.sort
  ans = 0
  keys.each_with_index do |a, i|
    (i...keys.length).each do |j|
      b = keys[j]
      c = target - a - b
      break if c < b
      next unless count.key?(c)

      if a == b && b == c
        ans += count[a] * (count[a] - 1) * (count[a] - 2) / 6
      elsif a == b
        ans += count[a] * (count[a] - 1) / 2 * count[c]
      elsif b == c
        ans += count[a] * count[b] * (count[b] - 1) / 2
      else
        ans += count[a] * count[b] * count[c]
      end
    end
  end
  ans % mod
end
