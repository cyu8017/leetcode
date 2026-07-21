
# @param {String} s
# @return {String}
def replace_digits(s)
  chars = s.chars
  (1...chars.length).step(2) do |i|
    chars[i] = (chars[i - 1].ord + chars[i].to_i).chr
  end
  chars.join
end
