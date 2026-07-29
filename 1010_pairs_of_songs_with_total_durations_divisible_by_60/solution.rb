# LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

# @param {Integer[]} time
# @return {Integer}
def num_pairs_divisible_by60(time)
  count = Array.new(60, 0)
  ans = 0
  time.each do |t|
    ans += count[-t % 60]
    count[t % 60] += 1
  end
  ans
end
