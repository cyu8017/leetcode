# LeetCode 3851 - Maximum Requests Without Violating the Limit
# https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

# @param {Integer[][]} requests
# @param {Integer} k
# @param {Integer} window
# @return {Integer}
def max_requests(requests, k, window)
  g = {}
  requests.each do |r|
    g[r[0]] ||= []
    g[r[0]] << r[1]
  end
  ans = requests.length
  g.each_value do |ts|
    ts.sort!
    kept = []
    ts.each do |t|
      kept.shift while !kept.empty? && t - kept[0] > window
      if kept.length < k
        kept << t
      else
        ans -= 1
      end
    end
  end
  ans
end
