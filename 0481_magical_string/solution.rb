# LeetCode 0481 - Magical String
# https://leetcode.com/problems/magical-string/

class Solution
  def magical_string(n)
    return 0 if n == 0

    seq = [1, 2, 2]
    i = 2
    while seq.length < n
      if seq[i] == 1
        seq << (seq[-1] == 2 ? 1 : 2)
      else
        next_val = seq[-1] == 2 ? 1 : 2
        seq.concat([next_val, next_val])
      end
      i += 1
    end
    seq[0, n].count(1)
  end

  alias_method :magicalString, :magical_string
end
