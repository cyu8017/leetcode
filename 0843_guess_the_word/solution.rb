# LeetCode 0843 - Guess the Word
# https://leetcode.com/problems/guess-the-word/

# @param {String[]} words
# @param {Object} master
# @return {Void}
def find_secret_word(words, master)
  return if master.nil? || !master.respond_to?(:guess)

  match = ->(a, b) { a.chars.zip(b.chars).count { |x, y| x == y } }

  candidates = words.dup
  until candidates.empty?
    best = candidates.min_by do |w|
      (0..6).map { |m| candidates.count { |c| match.call(w, c) == m } }.max
    end
    score = master.guess(best)
    return if score == 6

    candidates = candidates.select { |c| match.call(c, best) == score }
  end
end
