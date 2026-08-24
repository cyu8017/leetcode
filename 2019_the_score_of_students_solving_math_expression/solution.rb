# LeetCode 2019 - The Score of Students Solving Math Expression
# https://leetcode.com/problems/the-score-of-students-solving-math-expression/

# @param {String} s
# @param {Integer[]} answers
# @return {Integer}
def score_of_students(s, answers)
  eval_correct = lambda do |expr|
    nums = []
    ops = []
    expr.each_char do |c|
      if c >= "0" && c <= "9"
        nums << c.ord - 48
      else
        ops << c
      end
    end
    new_nums = [nums[0]]
    new_ops = []
    ops.each_with_index do |op, j|
      if op == "*"
        new_nums[-1] *= nums[j + 1]
      else
        new_ops << op
        new_nums << nums[j + 1]
      end
    end
    res = new_nums[0]
    new_ops.each_index { |j| res += new_nums[j + 1] }
    res
  end

  n = s.length
  correct = eval_correct.call(s)
  dp = Array.new(n) { Array.new(n) }

  dfs = lambda do |l, r|
    return dp[l][r] unless dp[l][r].nil?

    res = {}
    if l == r
      res[s[l].ord - 48] = true
      dp[l][r] = res
      return res
    end
    i = l + 1
    while i < r
      dfs.call(l, i - 1).each_key do |a|
        dfs.call(i + 1, r).each_key do |b|
          v = s[i] == "+" ? a + b : a * b
          res[v] = true if v <= 1000
        end
      end
      i += 2
    end
    dp[l][r] = res
    res
  end

  possible = dfs.call(0, n - 1)
  ans = 0
  answers.each do |a|
    if a == correct
      ans += 5
    elsif possible[a]
      ans += 2
    end
  end
  ans
end
