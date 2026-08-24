# LeetCode 2746 - Decremental String Concatenation
# https://leetcode.com/problems/decremental-string-concatenation/

# @param {String[]} words
# @return {Integer}
def minimize_concatenated_length(words)
  n = words.length
  memo = {}
  w0 = words[0]

  dfs = lambda do |i, first, last|
    return 0 if i == n
    key = [i, first, last]
    return memo[key] if memo.key?(key)
    w = words[i]
    wf, wl = w[0], w[-1]
    add1 = w.length - (last == wf ? 1 : 0)
    add2 = w.length - (wl == first ? 1 : 0)
    res = [add1 + dfs.call(i + 1, first, wl), add2 + dfs.call(i + 1, wf, last)].min
    memo[key] = res
    res
  end

  w0.length + dfs.call(1, w0[0], w0[-1])
end
