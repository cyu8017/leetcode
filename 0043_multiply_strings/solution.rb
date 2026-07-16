# LeetCode 0043 - Multiply Strings
# https://leetcode.com/problems/multiply-strings/

# @param {String} num1
# @param {String} num2
# @return {String}
def multiply(num1, num2)
  return "0" if num1 == "0" || num2 == "0"

  positions = Array.new(num1.length + num2.length, 0)

  (num1.length - 1).downto(0) do |i|
    (num2.length - 1).downto(0) do |j|
      product = num1[i].to_i * num2[j].to_i
      low = i + j + 1
      high = i + j
      total = product + positions[low]
      positions[low] = total % 10
      positions[high] += total / 10
    end
  end

  result = positions.map(&:to_s).join.sub(/\A0+/, "")
  result.empty? ? "0" : result
end
