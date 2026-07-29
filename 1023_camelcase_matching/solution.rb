# LeetCode 1023 - Camelcase Matching
# https://leetcode.com/problems/camelcase-matching/

# @param {String[]} queries
# @param {String} pattern
# @return {Boolean[]}
def camel_match(queries, pattern)
  matches = lambda do |q|
    i = 0
    q.each_char do |ch|
      if i < pattern.length && ch == pattern[i]
        i += 1
      elsif ch.match?(/[A-Z]/)
        return false
      end
    end
    i == pattern.length
  end
  queries.map { |q| matches.call(q) }
end
