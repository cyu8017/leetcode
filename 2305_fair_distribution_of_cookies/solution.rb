# LeetCode 2305 - Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/

# @param {Integer[]} cookies
# @param {Integer} k
# @return {Integer}
def distribute_cookies(cookies, k)
  bags = Array.new(k, 0)
  ans = [Float::INFINITY]
  dfs = lambda do |i|
    if i == cookies.length
      mx = bags.max
      ans[0] = mx if mx < ans[0]
      return
    end
    seen = {}
    bags.each_index do |j|
      next if seen[bags[j]]
      seen[bags[j]] = true
      bags[j] += cookies[i]
      dfs.call(i + 1) if bags[j] < ans[0]
      bags[j] -= cookies[i]
      break if bags[j] == 0
    end
  end
  dfs.call(0)
  ans[0].to_i
end
