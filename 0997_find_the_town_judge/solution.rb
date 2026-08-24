# LeetCode 0997 - Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/

# @param {Integer} n
# @param {Integer[][]} trust
# @return {Integer}
def find_judge(n, trust)
  score = Array.new(n + 1, 0)
  trust.each do |a, b|
    score[a] -= 1
    score[b] += 1
  end
  (1..n).each { |i| return i if score[i] == n - 1 }
  -1
end
