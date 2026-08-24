# LeetCode 2531 - Make Number of Distinct Characters Equal
# https://leetcode.com/problems/make-number-of-distinct-characters-equal/

# @param {String} word1
# @param {String} word2
# @return {Boolean}
def is_it_possible(word1, word2)
  c1 = Array.new(26, 0)
  c2 = Array.new(26, 0)
  word1.each_byte { |b| c1[b - 97] += 1 }
  word2.each_byte { |b| c2[b - 97] += 1 }
  d1 = d2 = 0
  26.times do |i|
    d1 += 1 if c1[i] > 0
    d2 += 1 if c2[i] > 0
  end
  26.times do |a|
    next if c1[a] == 0

    26.times do |b|
      next if c2[b] == 0

      nd1 = d1
      nd2 = d2
      if a == b
        return true if nd1 == nd2

        next
      end
      nd1 -= 1 if c1[a] == 1
      nd1 += 1 if c1[b] == 0
      nd2 -= 1 if c2[b] == 1
      nd2 += 1 if c2[a] == 0
      return true if nd1 == nd2
    end
  end
  false
end
