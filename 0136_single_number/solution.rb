class Solution
  def single_number(nums)
    nums.reduce(0, :^)
  end
end