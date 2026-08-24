# LeetCode 0818 - Race Car
# https://leetcode.com/problems/race-car/

# @param {Integer} target
# @return {Integer}
def racecar(target)
  queue = [[0, 1, 0]]
  seen = { [0, 1] => true }
  until queue.empty?
    pos, speed, steps = queue.shift
    return steps if pos == target

    nxt_pos = pos + speed
    nxt_speed = speed * 2
    if !seen[[nxt_pos, nxt_speed]] && nxt_pos.abs < target * 2
      seen[[nxt_pos, nxt_speed]] = true
      queue << [nxt_pos, nxt_speed, steps + 1]
    end
    rev_speed = speed > 0 ? -1 : 1
    unless seen[[pos, rev_speed]]
      seen[[pos, rev_speed]] = true
      queue << [pos, rev_speed, steps + 1]
    end
  end
  -1
end
