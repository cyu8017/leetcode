# LeetCode 2451 - Odd String Difference
# https://leetcode.com/problems/odd-string-difference/

# @param {String[]} words
# @return {String}
def odd_string(words)
  diff = lambda do |w|
    b = ""
    (1...w.length).each do |i|
      d = w[i].ord - w[i - 1].ord
      b << (d + 128).chr << ","
    end
    b
  end

  d0 = diff.call(words[0])
  d1 = diff.call(words[1])
  if d0 == d1
    (2...words.length).each { |i| return words[i] if diff.call(words[i]) != d0 }
  end
  return words[1] if diff.call(words[2]) == d0

  words[0]
end
