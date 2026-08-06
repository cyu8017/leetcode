# LeetCode 1342 - Number Of Steps To Reduce A Number To Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def number_of_steps(num)
  steps = 0
  while num > 0
    num = num.even? ? num / 2 : num - 1
    steps += 1
  end
  steps
end
