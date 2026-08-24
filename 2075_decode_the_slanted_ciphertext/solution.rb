# LeetCode 2075 - Decode the Slanted Ciphertext
# https://leetcode.com/problems/decode-the-slanted-ciphertext/

# @param {String} encoded_text
# @param {Integer} rows
# @return {String}
def decode_ciphertext(encoded_text, rows)
  return encoded_text if rows == 1

  cols = encoded_text.length / rows
  b = []
  cols.times do |c|
    rows.times do |r|
      break if c + r >= cols

      b << encoded_text[r * cols + c + r]
    end
  end
  b.pop while !b.empty? && b[-1] == " "
  b.join
end
