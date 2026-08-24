# LeetCode 3029 - Minimum Time to Revert Word to Initial State I
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_time_to_initial_state(word, k)
  n = word.length
  i = k
  while i < n
    return i / k if word[i..-1] == word[0, n - i]

    i += k
  end
  (n + k - 1) / k
end
