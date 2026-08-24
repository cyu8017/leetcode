# LeetCode 3076 - Shortest Uncommon Substring in an Array
# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

# @param {String[]} arr
# @return {String[]}
def shortest_substrings(arr)
  n = arr.length
  ans = Array.new(n, "")
  n.times do |i|
    s = arr[i]
    m = s.length
    j = 1
    while j <= m && ans[i] == ""
      (0..m - j).each do |l|
        sub = s[l, j]
        if ans[i] == "" || ans[i] > sub
          ok = true
          n.times do |k|
            if k != i && arr[k].include?(sub)
              ok = false
              break
            end
          end
          ans[i] = sub if ok
        end
      end
      j += 1
    end
  end
  ans
end
