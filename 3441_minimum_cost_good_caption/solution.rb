# LeetCode 3441 - Minimum Cost Good Caption
# https://leetcode.com/problems/minimum-cost-good-caption/

# @param {String} caption
# @return {String}
def min_cost_good_caption(caption)
  n = caption.length
  return "" if n < 3

  ans = caption.chars
  i = 0
  while i < n
    j = i
    j += 1 while j < n && ans[j] == ans[i]
    if j - i >= 3
      i = j
      next
    end
    need = 3 - (j - i)
    if j + need <= n
      (0...need).each { |t| ans[j + t] = ans[i] }
      i = j + need
    else
      ch = "a"
      if i > 0
        ch = ans[i - 1]
      elsif j < n
        ch = caption[j]
      end
      (i...n).each { |t| ans[t] = ch }
      break
    end
  end
  i = 0
  while i < n
    j = i
    j += 1 while j < n && ans[j] == ans[i]
    return "" if j - i < 3

    i = j
  end
  ans.join
end
