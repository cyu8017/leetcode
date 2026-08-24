# LeetCode 2092 - Find All People With Secret
# https://leetcode.com/problems/find-all-people-with-secret/

# @param {Integer} n
# @param {Integer[][]} meetings
# @param {Integer} first_person
# @return {Integer[]}
def find_all_people(n, meetings, first_person)
  meetings.sort_by! { |m| m[2] }
  parent = (0...n).to_a

  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end

  unite = lambda do |a, b|
    a = find.call(a)
    b = find.call(b)
    parent[a] = b if a != b
  end

  know = Array.new(n, false)
  know[0] = know[first_person] = true
  unite.call(0, first_person)
  i = 0
  while i < meetings.length
    j = i
    j += 1 while j < meetings.length && meetings[j][2] == meetings[i][2]
    (i...j).each { |k| unite.call(meetings[k][0], meetings[k][1]) }
    root0 = find.call(0)
    reset = []
    (i...j).each do |k|
      a = meetings[k][0]
      b = meetings[k][1]
      if find.call(a) != root0
        reset << a
        reset << b
      else
        know[a] = know[b] = true
      end
    end
    reset.each { |x| parent[x] = x }
    i = j
  end
  (0...n).select { |x| find.call(x) == find.call(0) || know[x] }
end
