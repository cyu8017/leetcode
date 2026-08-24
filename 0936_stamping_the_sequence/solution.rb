# LeetCode 0936 - Stamping the Sequence
# https://leetcode.com/problems/stamping-the-sequence/

# @param {String} stamp
# @param {String} target
# @return {Integer[]}
def moves_to_stamp(stamp, target)
  n = target.length
  m = stamp.length
  done = Array.new(n, false)
  ans = []
  changed = true
  while changed
    changed = false
    (0..(n - m)).each do |i|
      ok = (0...m).all? { |j| done[i + j] || target[i + j] == stamp[j] }
      if ok && (0...m).any? { |j| !done[i + j] }
        m.times { |j| done[i + j] = true }
        ans << i
        changed = true
        break
      end
    end
  end
  done.all? ? ans.reverse : []
end
