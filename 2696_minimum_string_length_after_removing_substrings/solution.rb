# LeetCode 2696 - Minimum String Length After Removing Substrings
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

# @param {String} s
# @return {Integer}
def min_length(s)
  st = []
  s.each_char do |c|
    last = st.empty? ? nil : st[-1]
    if !st.empty? && ((last == "A" && c == "B") || (last == "C" && c == "D"))
      st.pop
    else
      st << c
    end
  end
  st.length
end
