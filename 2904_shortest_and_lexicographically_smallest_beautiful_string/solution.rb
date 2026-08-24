# LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def shortest_beautiful_substring(s, k)
  ans = ""
  n = s.length
  (0...n).each do |i|
    ones = 0
    (i...n).each do |j|
      ones += 1 if s[j] == "1"
      if ones == k
        cand = s[i..j]
        if ans.empty? || cand.length < ans.length || (cand.length == ans.length && cand < ans)
          ans = cand
        end
        break
      end
      break if ones > k
    end
  end
  ans
end
