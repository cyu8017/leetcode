# LeetCode 0278 - First Bad Version
# https://leetcode.com/problems/first-bad-version/

def is_bad_version(_version)
  false
end

class Solution
  def firstBadVersion(n)
    left = 1
    right = n
    while left < right
      mid = left + (right - left) / 2
      if is_bad_version(mid)
        right = mid
      else
        left = mid + 1
      end
    end
    left
  end
end
