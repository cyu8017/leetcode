# LeetCode 2468 - Split Message Based on Limit
# https://leetcode.com/problems/split-message-based-on-limit/

# @param {String} message
# @param {Integer} limit
# @return {String[]}
def split_message(message, limit)
  n = message.length
  (1..n).each do |parts|
    sb_digits = parts.to_s.length
    ok = true
    idx = 0
    res = []
    (1..parts).each do |i|
      tail = 3 + i.to_s.length + sb_digits
      cap = limit - tail
      if cap <= 0 || idx >= n
        ok = false
        break
      end
      take = cap
      take = n - idx if take > n - idx
      res << message[idx, take] + "<" + i.to_s + "/" + parts.to_s + ">"
      idx += take
    end
    return res if ok && idx == n
  end
  []
end
