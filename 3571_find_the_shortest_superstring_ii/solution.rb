# LeetCode 3571 - Find the Shortest Superstring II
# https://leetcode.com/problems/find-the-shortest-superstring-ii/

# @param {String} s1
# @param {String} s2
# @return {String}
def shortest_superstring(s1, s2)
  return shortest_superstring(s2, s1) if s1.length > s2.length
  m = s1.length
  return s2 if s2.include?(s1)
  (0...m).each do |i|
    return s1[0...i] + s2 if s2.start_with?(s1[i..])
    length = m - i
    if s2.length >= length && s2[-length..] == s1[0...length]
      return s2 + s1[(m - i)..]
    end
  end
  s1 + s2
end
