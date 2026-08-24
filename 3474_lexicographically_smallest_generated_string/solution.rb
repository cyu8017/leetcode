# LeetCode 3474 - Lexicographically Smallest Generated String
# https://leetcode.com/problems/lexicographically-smallest-generated-string/

# @param {String} str1
# @param {String} str2
# @return {String}
def generate_string(str1, str2)
  n = str1.length
  m = str2.length
  len = n + m - 1
  ans = Array.new(len, "?")
  (0...n).each do |i|
    next unless str1[i] == "T"

    (0...m).each do |j|
      return "" if ans[i + j] != "?" && ans[i + j] != str2[j]

      ans[i + j] = str2[j]
    end
  end
  (0...len).each { |i| ans[i] = "a" if ans[i] == "?" }
  (0...n).each do |i|
    next unless str1[i] == "F"

    match = true
    (0...m).each do |j|
      if ans[i + j] != str2[j]
        match = false
        break
      end
    end
    next unless match

    changed = false
    (m - 1).downto(0) do |j|
      pos = i + j
      forced = false
      (0...n).each do |t|
        if str1[t] == "T" && pos >= t && pos < t + m
          forced = true
          break
        end
      end
      next if forced

      ans[pos] = "b"
      changed = true
      break
    end
    return "" unless changed
  end
  (0...n).each do |i|
    match = true
    (0...m).each do |j|
      if ans[i + j] != str2[j]
        match = false
        break
      end
    end
    return "" if str1[i] == "T" && !match
    return "" if str1[i] == "F" && match
  end
  ans.join
end
