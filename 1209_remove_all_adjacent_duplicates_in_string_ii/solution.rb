# LeetCode 1209 - Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# @param {String} s
# @param {Integer} k
# @return {String}
def remove_duplicates(s, k)
  stack = []
  s.each_char do |ch|
    if !stack.empty? && stack[-1][0] == ch
      stack[-1][1] += 1
    else
      stack << [ch, 1]
    end
    stack.pop if stack[-1][1] == k
  end
  stack.map { |ch, count| ch * count }.join
end
