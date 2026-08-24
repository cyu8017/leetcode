# LeetCode 0633 - Sum of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers/

# @param {Integer} c
# @return {Boolean}
def judge_square_sum(c)
  left = 0
  right = Integer.sqrt(c)
  while left <= right
    total = left * left + right * right
    return true if total == c

    if total < c
      left += 1
    else
      right -= 1
    end
  end
  false
end
