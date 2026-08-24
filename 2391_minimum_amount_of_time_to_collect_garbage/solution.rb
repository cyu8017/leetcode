# LeetCode 2391 - Minimum Amount of Time to Collect Garbage
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

# @param {String[]} garbage
# @param {Integer[]} travel
# @return {Integer}
def garbage_collection(garbage, travel)
  ans = 0
  last_m = 0
  last_p = 0
  last_g = 0
  garbage.each_with_index do |g, i|
    ans += g.length
    g.each_char do |c|
      if c == "M"
        last_m = i
      elsif c == "P"
        last_p = i
      else
        last_g = i
      end
    end
  end
  pref = Array.new(travel.length + 1, 0)
  travel.each_index { |i| pref[i + 1] = pref[i] + travel[i] }
  ans + pref[last_m] + pref[last_p] + pref[last_g]
end
