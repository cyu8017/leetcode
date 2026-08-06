# LeetCode 1538 - Guess the Majority in a Hidden Array
# https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

class ArrayReader
  def initialize(nums)
    @nums = nums
  end

  def query(a, b, c, d)
    ones = @nums[a] + @nums[b] + @nums[c] + @nums[d]
    return 4 if ones == 0 || ones == 4
    return 2 if ones == 1 || ones == 3
    0
  end

  def length
    @nums.length
  end
end

# @param {ArrayReader|Integer[]} reader
# @return {Integer}
def guess_majority(reader)
  reader = ArrayReader.new(reader) if reader.is_a?(Array)
  n = reader.length
  first_four = reader.query(0, 1, 2, 3)
  shifted = reader.query(1, 2, 3, 4)
  same = 1
  different = 0
  different_index = -1
  later_different = -1
  four_same = first_four == shifted
  if four_same
    same += 1
  else
    different += 1
    different_index = 4
  end
  [[0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4]].each_with_index do |args, idx|
    if reader.query(*args) == shifted
      same += 1
    else
      different += 1
      different_index = idx + 1
    end
  end
  (5...n).each do |i|
    i_same_as_four = reader.query(1, 2, 3, i) == shifted
    if i_same_as_four == four_same
      same += 1
    else
      different += 1
      different_index = i
      later_different = i if later_different == -1
    end
  end
  return -1 if same == different
  same > different ? 0 : (later_different != -1 ? later_different : different_index)
end
