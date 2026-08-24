# LeetCode 2140 - Solving Questions With Brainpower
# https://leetcode.com/problems/solving-questions-with-brainpower/

# @param {Integer[][]} questions
# @return {Integer}
def most_points(questions)
  n = questions.length
  dp = Array.new(n + 1, 0)
  (n - 1).downto(0) do |i|
    pts, brain = questions[i]
    nxt = i + brain + 1
    take = pts + (nxt < n ? dp[nxt] : 0)
    dp[i] = [dp[i + 1], take].max
  end
  dp[0]
end
