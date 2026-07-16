# LeetCode 0187 - Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/

require "set"

# @param {String} s
# @return {String[]}
def find_repeated_dna_sequences(s)
  return [] if s.length < 10

  seen = Set.new
  repeated = Set.new

  (0..s.length - 10).each do |index|
    sequence = s[index, 10]
    if seen.include?(sequence)
      repeated.add(sequence)
    else
      seen.add(sequence)
    end
  end

  repeated.to_a
end