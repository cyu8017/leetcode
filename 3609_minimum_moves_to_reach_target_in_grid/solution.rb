# LeetCode 3609 - Minimum Moves to Reach Target in Grid
# https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/

# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} tx
# @param {Integer} ty
# @return {Integer}
def min_moves(sx, sy, tx, ty)
  ans = 0
  while tx > sx || ty > sy
    return -1 if tx < sx || ty < sy
    return -1 if tx == ty
    if tx > ty
      if ty > sy
        if tx >= 2 * ty
          return -1 if tx.odd?
          tx /= 2
        else
          tx -= ty
        end
        ans += 1
      else
        return -1 if ty != sy
        while tx > sx
          if tx >= 2 * ty
            return -1 if tx.odd?
            tx /= 2
          else
            tx -= ty
          end
          ans += 1
          return -1 if tx < sx
        end
      end
    else
      if tx > sx
        if ty >= 2 * tx
          return -1 if ty.odd?
          ty /= 2
        else
          ty -= tx
        end
        ans += 1
      else
        return -1 if tx != sx
        while ty > sy
          if ty >= 2 * tx
            return -1 if ty.odd?
            ty /= 2
          else
            ty -= tx
          end
          ans += 1
          return -1 if ty < sy
        end
      end
    end
  end
  tx == sx && ty == sy ? ans : -1
end
