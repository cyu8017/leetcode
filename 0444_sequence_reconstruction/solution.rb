# LeetCode 0444 - Sequence Reconstruction
# https://leetcode.com/problems/sequence-reconstruction/

require "set"

class Solution
  def sequence_reconstruction(nums, sequences)
    indegree = nums.to_h { |value| [value, 0] }
    graph = nums.to_h { |value| [value, Set.new] }
    seen_edges = Set.new

    sequences.each do |sequence|
      (0...(sequence.length - 1)).each do |index|
        left = sequence[index]
        right = sequence[index + 1]
        next if seen_edges.include?([left, right])

        seen_edges.add([left, right])
        graph[left].add(right)
        indegree[right] += 1
      end
    end

    queue = nums.select { |value| indegree[value].zero? }
    order = []
    until queue.empty?
      return false if queue.length > 1

      node = queue.shift
      order << node
      graph[node].each do |neighbor|
        indegree[neighbor] -= 1
        queue << neighbor if indegree[neighbor].zero?
      end
    end

    order == nums
  end

  alias_method :sequenceReconstruction, :sequence_reconstruction
end
