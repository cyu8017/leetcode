# LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def minimum_operations_to_make_equal(x, y)
  return y - x if x <= y

  q = [[x, 0]]
  seen = { x => true }
  qi = 0
  while qi < q.length
    v, d = q[qi]
    qi += 1
    return d if v == y

    cands = [v + 1, v - 1]
    cands << (v / 11) if v % 11 == 0
    cands << (v / 5) if v % 5 == 0
    cands.each do |nxt|
      if nxt > 0 && nxt < 2 * x + 20 && !seen[nxt]
        seen[nxt] = true
        q << [nxt, d + 1]
      end
    end
  end
  -1
end
