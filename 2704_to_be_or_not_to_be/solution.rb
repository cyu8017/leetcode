# LeetCode 2704 - To Be Or Not To Be
# https://leetcode.com/problems/to-be-or-not-to-be/

# @param {Object} val
# @return {Hash}
def expect(val)
  {
    "toBe" => lambda do |other|
      return true if val == other

      raise "Not Equal"
    end,
    "notToBe" => lambda do |other|
      return true if val != other

      raise "Equal"
    end
  }
end
