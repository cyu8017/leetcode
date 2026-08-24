# LeetCode 0702 - Search in a Sorted Array of Unknown Size
# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

class ArrayReader
  def initialize(secret)
    @secret = secret
  end

  def get(index)
    return 2**31 - 1 if index < 0 || index >= @secret.length

    @secret[index]
  end
end

# @param {ArrayReader} reader
# @param {Integer} target
# @return {Integer}
def search(reader, target)
  reader = ArrayReader.new(reader) if reader.is_a?(Array)

  right = 1
  right <<= 1 while reader.get(right) < target
  left = right >> 1

  while left <= right
    mid = (left + right) / 2
    value = reader.get(mid)
    return mid if value == target

    if value > target
      right = mid - 1
    else
      left = mid + 1
    end
  end
  -1
end
