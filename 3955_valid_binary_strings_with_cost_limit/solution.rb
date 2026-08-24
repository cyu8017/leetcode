# LeetCode 3955 - Valid Binary Strings With Cost Limit
# https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

# @param {Integer} n
# @param {Integer} k
# @return {String[]}
def generate_valid_strings(n, k)
  ans = []
  path = []
  dfs = nil
  dfs = lambda do |i, tot|
    if i >= n
      ans << path.join
      return
    end
    path << "0"
    dfs.call(i + 1, tot)
    path.pop
    if (path.empty? || path[-1] == "0") && tot + i <= k
      path << "1"
      dfs.call(i + 1, tot + i)
      path.pop
    end
  end
  dfs.call(0, 0)
  ans
end
