# LeetCode 1404 - Number Of Steps To Reduce A Number In Binary Representation To One
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

def num_steps(s)
  steps = carry = 0
  s[1..].reverse.each_char do |bit|
    value = bit.to_i + carry
    if value == 1
      steps += 2
      carry = 1
    else
      steps += 1
    end
  end
  steps + carry
end
