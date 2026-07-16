# LeetCode 0072 - Edit Distance
# https://leetcode.com/problems/edit-distance/

# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
  m = word1.length
  n = word2.length
  prev = (0..n).to_a
  curr = Array.new(n + 1, 0)

  (1..m).each do |i|
    curr[0] = i
    (1..n).each do |j|
      curr[j] = if word1[i - 1] == word2[j - 1]
                  prev[j - 1]
                else
                  1 + [prev[j], curr[j - 1], prev[j - 1]].min
                end
    end
    prev, curr = curr, prev
  end

  prev[n]
end
