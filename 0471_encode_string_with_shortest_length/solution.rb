# LeetCode 0471 - Encode String with Shortest Length
# https://leetcode.com/problems/encode-string-with-shortest-length/

class Solution
  def encode(s)
    length = s.length
    dp = Array.new(length + 1, "")

    encode_word = lambda do |word|
      size = word.length
      best = word
      (1..size / 2).each do |unit_length|
        next unless size % unit_length == 0

        unit = word[0, unit_length]
        if unit * (size / unit_length) == word
          encoded = "#{size / unit_length}[#{unit}]"
          if encoded.length < best.length || (encoded.length == best.length && encoded < best)
            best = encoded
          end
        end
      end
      best
    end

    (1..length).each do |index|
      dp[index] = encode_word.call(s[0, index])
      (1...index).each do |split|
        candidate = dp[index - split] + encode_word.call(s[index - split, split])
        if candidate.length < dp[index].length || (candidate.length == dp[index].length && candidate < dp[index])
          dp[index] = candidate
        end
      end
    end
    dp[length]
  end
end
