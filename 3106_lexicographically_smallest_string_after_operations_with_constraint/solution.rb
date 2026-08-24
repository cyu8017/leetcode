# LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

# @param {String} s
# @param {Integer} k
# @return {String}
def get_smallest_string(s, k)
  arr = s.chars
  arr.each_index do |i|
    c1 = arr[i].ord
    (97...c1).each do |c2|
      d = [c1 - c2, 26 - (c1 - c2)].min
      if d <= k
        arr[i] = c2.chr
        k -= d
        break
      end
    end
  end
  arr.join
end
