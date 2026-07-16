# LeetCode 0271 - Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/

class Codec
  def encode(strs)
    strs.map { |text| "#{text.length}##{text}" }.join
  end

  def decode(encoded)
    result = []
    index = 0
    while index < encoded.length
      delimiter = encoded.index("#", index)
      length = encoded[index...delimiter].to_i
      start = delimiter + 1
      result << encoded[start, length]
      index = start + length
    end
    result
  end
end
