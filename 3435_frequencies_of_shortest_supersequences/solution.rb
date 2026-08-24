# LeetCode 3435 - Frequencies of Shortest Supersequences
# https://leetcode.com/problems/frequencies-of-shortest-supersequences/

# @param {String[]} words
# @return {Integer[][]}
def supersequences(words)
  used = Array.new(26, false)
  words.each do |w|
    used[w[0].ord - 97] = true
    used[w[1].ord - 97] = true
  end
  letters = (0...26).select { |i| used[i] }
  m = letters.length
  freq = Array.new(26, 0)
  best = 10**9
  best_freqs = []
  dfs = nil
  dfs = lambda do |i|
    if i == m
      words.each do |w|
        a = w[0].ord - 97
        b = w[1].ord - 97
        if a == b
          return if freq[a] < 2
        elsif freq[a] < 1 || freq[b] < 1
          return
        end
      end
      s = freq.sum
      f = freq.dup
      if s < best
        best = s
        best_freqs = [f]
      elsif s == best
        best_freqs << f
      end
      return
    end
    l = letters[i]
    (1..2).each do |c|
      freq[l] = c
      dfs.call(i + 1)
    end
    freq[l] = 0
  end
  dfs.call(0)
  best_freqs
end
