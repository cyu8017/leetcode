# LeetCode 2591 - Distribute Money to Maximum Children
# https://leetcode.com/problems/distribute-money-to-maximum-children/

# @param {Integer} money
# @param {Integer} children
# @return {Integer}
def dist_money(money, children)
  return -1 if money < children

  money -= children
  ans = money / 7
  ans = children if ans > children
  remain_money = money - ans * 7
  remain_child = children - ans
  if remain_child == 0 && remain_money > 0
    ans -= 1
  elsif remain_child == 1 && remain_money == 3
    ans -= 1
  end
  return 0 if ans < 0

  ans
end
