class Solution
  def single_number(nums)
    ones = 0
    twos = 0
    nums.each do |num|
      ones = (ones ^ num) & ~twos
      twos = (twos ^ num) & ~ones
    end
    ones
  end
end