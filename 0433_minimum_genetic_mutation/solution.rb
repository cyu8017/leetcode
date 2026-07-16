# LeetCode 0433 - Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/

require "set"

class Solution
  def min_mutation(start_gene, end_gene, bank)
    return 0 if start_gene == end_gene

    valid = bank.to_set
    return -1 unless valid.include?(end_gene)

    genes = "ACGT"
    queue = [[start_gene, 0]]
    visited = { start_gene => true }

    until queue.empty?
      gene, steps = queue.shift
      return steps if gene == end_gene

      chars = gene.chars
      chars.length.times do |index|
        original = chars[index]
        genes.each_char do |letter|
          next if letter == original

          chars[index] = letter
          candidate = chars.join
          if valid.include?(candidate) && !visited[candidate]
            visited[candidate] = true
            queue << [candidate, steps + 1]
          end
          chars[index] = original
        end
      end
    end

    -1
  end

  alias_method :minMutation, :min_mutation
end
