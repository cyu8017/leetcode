# LeetCode 0780 - Reaching Points
# https://leetcode.com/problems/reaching-points/

# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} tx
# @param {Integer} ty
# @return {Boolean}
def reaching_points(sx, sy, tx, ty)
  while tx >= sx && ty >= sy
    return true if tx == sx && ty == sy
    break if tx == ty

    if tx > ty
      if ty > sy
        tx %= ty
      else
        return (tx - sx) % ty == 0
      end
    elsif tx > sx
      ty %= tx
    else
      return (ty - sy) % tx == 0
    end
  end
  tx == sx && ty == sy
end
