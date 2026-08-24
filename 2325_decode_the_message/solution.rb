# LeetCode 2325 - Decode the Message
# https://leetcode.com/problems/decode-the-message/

# @param {String} key
# @param {String} message
# @return {String}
def decode_message(key, message)
  mp = Array.new(26, 0)
  nxt = 97
  key.each_char do |c|
    next if c == " " || mp[c.ord - 97] != 0
    mp[c.ord - 97] = nxt
    nxt += 1
  end
  out = message.chars
  out.each_index do |i|
    out[i] = mp[out[i].ord - 97].chr if out[i] != " "
  end
  out.join
end
