# LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

# @param {String} w1
# @param {String} w2
# @param {Integer} i
# @param {Integer} j
# @param {Boolean} used_skip
# @param {Integer[]} right
# @return {Boolean}
def can_finish_valid_sequence(w1, w2, i, j, used_skip, right)
  m = w2.length
  return true if j >= m
  unless used_skip
    return true if right[j] >= i
    return true if j + 1 <= m && right[j + 1] > i
    return true if right[j] > i

    return false
  end
  right[j] >= i
end

# @param {String} word1
# @param {String} word2
# @return {Integer[]}
def valid_sequence(word1, word2)
  n = word1.length
  m = word2.length
  right = Array.new(m + 1, 0)
  right[m] = n
  j = m - 1
  i = n - 1
  while i >= 0 && j >= 0
    if word1[i] == word2[j]
      right[j] = i
      j -= 1
    end
    i -= 1
  end
  while j >= 0
    right[j] = -1
    j -= 1
  end
  ans = Array.new(m, 0)
  used_skip = false
  i = 0
  m.times do |jj|
    found = false
    while i < n
      if word1[i] == word2[jj]
        if can_finish_valid_sequence(word1, word2, i + 1, jj + 1, used_skip, right)
          ans[jj] = i
          i += 1
          found = true
          break
        end
      elsif !used_skip
        if can_finish_valid_sequence(word1, word2, i + 1, jj + 1, true, right)
          ans[jj] = i
          i += 1
          used_skip = true
          found = true
          break
        end
      end
      i += 1
    end
    return [] unless found
  end
  ans
end
