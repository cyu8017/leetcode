# LeetCode 0650 - 2 Keys Keyboard
# https://leetcode.com/problems/2-keys-keyboard/

# @param {Integer} n
# @return {Integer}
def min_steps(n)
  steps = 0
  factor = 2
  while factor * factor <= n
    while n % factor == 0
      steps += factor
      n /= factor
    end
    factor += 1
  end
  steps += n if n > 1
  steps
end
