# LeetCode 1898 - Maximum Number of Removable Characters
# https://leetcode.com/problems/maximum-number-of-removable-characters/

# @param {String} s
# @param {String} p
# @param {Integer[]} removable
# @return {Integer}
def maximum_removals(s, p, removable)
  still_subsequence = lambda do |k|
    removed = removable[0...k].to_h { |pos| [pos, true] }
    index = 0
    s.each_char.with_index do |char, position|
      next if removed[position]
      if index < p.length && char == p[index]
        index += 1
      end
    end
    index == p.length
  end

  lo = 0
  hi = removable.length
  while lo < hi
    mid = (lo + hi + 1) / 2
    if still_subsequence.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
