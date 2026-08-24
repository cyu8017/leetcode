# LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
# https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

# @param {Integer[][]} items
# @param {Integer} k
# @return {Integer}
def find_maximum_elegance(items, k)
  items = items.sort_by { |it| -it[0] }
  seen = {}
  total = 0
  dup = []
  (0...k).each do |i|
    total += items[i][0]
    c = items[i][1]
    if seen[c]
      dup << items[i][0]
    else
      seen[c] = true
    end
  end
  ans = total + seen.length * seen.length
  (k...items.length).each do |i|
    c = items[i][1]
    next if seen[c] || dup.empty?
    total += items[i][0] - dup.pop
    seen[c] = true
    ans = [ans, total + seen.length * seen.length].max
  end
  ans
end
