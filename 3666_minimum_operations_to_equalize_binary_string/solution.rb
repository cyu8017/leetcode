# LeetCode 3666 - Minimum Operations to Equalize Binary String
# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

require "set"

# @param {String} s
# @param {Integer} k
# @return {Integer}
def min_operations(s, k)
  n = s.length
  ts = [Set.new, Set.new]
  (0..n).each { |i| ts[i % 2] << i }
  cnt0 = s.count("0")
  ts[cnt0 % 2].delete(cnt0)
  q = [cnt0]
  ans = 0
  until q.empty?
    nq = []
    q.each do |cur|
      return ans if cur == 0

      l = cur + k - 2 * [cur, k].min
      r = cur + k - 2 * [k - n + cur, 0].max
      t = ts[l % 2]
      t.to_a.sort.each do |it|
        next if it < l
        break if it > r

        nq << it
        t.delete(it)
      end
    end
    q = nq
    ans += 1
  end
  -1
end
