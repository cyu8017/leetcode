# LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_strings(s1, s2)
  even1 = Array.new(26, 0)
  odd1 = Array.new(26, 0)
  even2 = Array.new(26, 0)
  odd2 = Array.new(26, 0)
  (0...s1.length).each do |i|
    if i.even?
      even1[s1[i].ord - 97] += 1
      even2[s2[i].ord - 97] += 1
    else
      odd1[s1[i].ord - 97] += 1
      odd2[s2[i].ord - 97] += 1
    end
  end
  even1 == even2 && odd1 == odd2
end
