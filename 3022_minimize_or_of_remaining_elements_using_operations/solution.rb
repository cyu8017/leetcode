# LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
# https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_or_after_operations(nums, k)
  ans = 0
  rans = 0
  29.downto(0) do |i|
    test = ans + (1 << i)
    cnt = 0
    val = 0
    nums.each do |num|
      if val == 0
        val = test & num
      else
        val &= test & num
      end
      cnt += 1 if val != 0
    end
    if cnt > k
      rans += 1 << i
    else
      ans += 1 << i
    end
  end
  rans
end
