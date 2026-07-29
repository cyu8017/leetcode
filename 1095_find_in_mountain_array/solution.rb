# LeetCode 1095 - Find in Mountain Array
# https://leetcode.com/problems/find-in-mountain-array/

# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# class MountainArray
#   def get(index)
#   end
#
#   def length
#   end
# end

# @param {Integer} target
# @param {MountainArray} mountain_arr
# @return {Integer}
def find_in_mountain_array(target, mountain_arr)
  n = mountain_arr.length
  lo = 0
  hi = n - 1
  while lo < hi
    mid = (lo + hi) / 2
    if mountain_arr.get(mid) < mountain_arr.get(mid + 1)
      lo = mid + 1
    else
      hi = mid
    end
  end
  peak = lo

  lo = 0
  hi = peak
  while lo <= hi
    mid = (lo + hi) / 2
    val = mountain_arr.get(mid)
    return mid if val == target

    if val < target
      lo = mid + 1
    else
      hi = mid - 1
    end
  end

  lo = peak + 1
  hi = n - 1
  while lo <= hi
    mid = (lo + hi) / 2
    val = mountain_arr.get(mid)
    return mid if val == target

    if val > target
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  -1
end
