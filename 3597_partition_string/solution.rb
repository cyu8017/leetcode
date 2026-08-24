# LeetCode 3597 - Partition String
# https://leetcode.com/problems/partition-string/

# @param {String} s
# @return {String[]}
def partition_string(s)
  vis = {}
  ans = []
  t = ""
  s.each_char do |c|
    t += c
    unless vis[t]
      vis[t] = true
      ans << t
      t = ""
    end
  end
  ans
end
