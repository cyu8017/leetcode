# LeetCode 2355 - Maximum Number of Books You Can Take
# https://leetcode.com/problems/maximum-number-of-books-you-can-take/

# @param {Integer[]} books
# @return {Integer}
def maximum_books(books)
  n = books.length
  dp = Array.new(n, 0)
  stack = []
  interval_sum = lambda do |l, r, h|
    width = r - l + 1
    return width * (2 * h - width + 1) / 2 if h >= width
    h * (h + 1) / 2
  end
  ans = 0
  (0...n).each do |i|
    stack.pop while !stack.empty? && books[stack[-1]] >= books[i] - (i - stack[-1])
    if stack.empty?
      dp[i] = interval_sum.call(0, i, books[i])
    else
      j = stack[-1]
      dp[i] = dp[j] + interval_sum.call(j + 1, i, books[i])
    end
    ans = dp[i] if dp[i] > ans
    stack << i
  end
  ans
end

alias solve maximum_books
