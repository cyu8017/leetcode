# LeetCode 0752 - Open the Lock
# https://leetcode.com/problems/open-the-lock/

# @param {String[]} deadends
# @param {String} target
# @return {Integer}
def open_lock(deadends, target)
  dead = {}
  deadends.each { |d| dead[d] = true }
  return -1 if dead["0000"]

  queue = [["0000", 0]]
  seen = { "0000" => true }
  until queue.empty?
    state, steps = queue.shift
    return steps if state == target

    4.times do |i|
      digit = state[i].to_i
      [-1, 1].each do |delta|
        nxt = state.dup
        nxt[i] = ((digit + delta) % 10).to_s
        next if seen[nxt] || dead[nxt]

        seen[nxt] = true
        queue << [nxt, steps + 1]
      end
    end
  end
  -1
end
