# LeetCode 0022 - Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

# @param {Integer} n
# @return {String[]}
def generate_parenthesis(n)
  result = []

  backtrack = lambda do |path, open_count, close_count|
    if path.length == 2 * n
      result << path
      return
    end
    if open_count < n
      backtrack.call(path + "(", open_count + 1, close_count)
    end
    if close_count < open_count
      backtrack.call(path + ")", open_count, close_count + 1)
    end
  end

  backtrack.call("", 0, 0)
  result
end
