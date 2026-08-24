# LeetCode 3638 - Maximum Balanced Shipments
# https://leetcode.com/problems/maximum-balanced-shipments/

# @param {Integer[]} weight
# @return {Integer}
def max_balanced_shipments(weight)
  ans = 0
  mx = 0
  weight.each do |x|
    mx = x if x > mx
    if x < mx
      ans += 1
      mx = 0
    end
  end
  ans
end
