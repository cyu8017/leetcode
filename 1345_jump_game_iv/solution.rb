# LeetCode 1345 - Jump Game Iv
# https://leetcode.com/problems/jump-game-iv/

def min_jumps(arr)
  positions = Hash.new { |h, k| h[k] = [] }
  arr.each_with_index { |value, i| positions[value] << i }
  queue = [0]
  seen = { 0 => true }
  steps = 0
  until queue.empty?
    queue.length.times do
      i = queue.shift
      return steps if i == arr.length - 1
      neighbors = positions.delete(arr[i]) || []
      neighbors += [i - 1, i + 1]
      neighbors.each do |j|
        next unless j >= 0 && j < arr.length && !seen[j]
        seen[j] = true
        queue << j
      end
    end
    steps += 1
  end
  -1
end
