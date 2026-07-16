# LeetCode 0514 - Freedom Trail
# https://leetcode.com/problems/freedom-trail/

class Solution
  def find_rotate_steps(ring, key)
    positions = Hash.new { |hash, char| hash[char] = [] }
    ring.each_char.with_index { |char, index| positions[char] << index }

    memo = {}
    dp = lambda do |ring_index, key_index|
      return 0 if key_index == key.length

      state = [ring_index, key_index]
      return memo[state] if memo.key?(state)

      best = Float::INFINITY
      positions[key[key_index]].each do |pos|
        clockwise = (pos - ring_index) % ring.length
        counter = (ring_index - pos) % ring.length
        steps = [clockwise, counter].min + 1
        best = [best, steps + dp.call(pos, key_index + 1)].min
      end
      memo[state] = best
    end

    dp.call(0, 0)
  end

  alias_method :findRotateSteps, :find_rotate_steps
end
