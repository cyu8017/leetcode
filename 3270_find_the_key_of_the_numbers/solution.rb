# LeetCode 3270 - Find the Key of the Numbers
# https://leetcode.com/problems/find-the-key-of-the-numbers/

# @param {Integer} num1
# @param {Integer} num2
# @param {Integer} num3
# @return {Integer}
def generate_key(num1, num2, num3)
  ans = 0
  mul = 1
  4.times do
    d = [num1 % 10, num2 % 10, num3 % 10].min
    ans += d * mul
    mul *= 10
    num1 /= 10
    num2 /= 10
    num3 /= 10
  end
  ans
end
