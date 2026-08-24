# LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
# https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

# @param {String} road
# @param {Integer} budget
# @return {Integer}
def max_potholes(road, budget)
  road = road + "."
  n = road.length
  cnt = Array.new(n, 0)
  k = 0
  ans = 0
  road.each_char do |c|
    if c == "x"
      k += 1
    elsif k > 0
      cnt[k] += 1
      k = 0
    end
  end
  k = n - 1
  while k > 0 && budget > 0
    t = [budget / (k + 1), cnt[k]].min
    ans += t * k
    budget -= t * (k + 1)
    cnt[k - 1] += cnt[k] - t
    k -= 1
  end
  ans
end
