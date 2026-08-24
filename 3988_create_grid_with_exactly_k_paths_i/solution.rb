# LeetCode 3988 - Create Grid With Exactly K Paths I
# https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

# @param {Integer} m
# @param {Integer} n
# @param {Integer} k
# @return {String[]}
def create_grid(m, n, k)
  cands = []
  if k == 1
    cands << ["."]
  elsif k == 2
    cands << ["..", ".."]
  elsif k == 3
    cands << ["..", "..", ".."]
    cands << ["...", "..."]
  elsif k == 4
    cands << ["..", "..", "..", ".."]
    cands << ["....", "...."]
    cands << ["..#", "...", "#.."]
  end
  cands.each do |pat|
    pr = pat.length
    pc = pat[0].length
    next if pr > m || pc > n
    result = Array.new(m) { "#" * n }
    pr.times do |i|
      row = result[i].chars
      pc.times { |j| row[j] = pat[i][j] }
      result[i] = row.join
    end
    (pr...m).each do |i|
      row = result[i].chars
      row[pc - 1] = "."
      result[i] = row.join
    end
    (pc...n).each do |j|
      row = result[m - 1].chars
      row[j] = "."
      result[m - 1] = row.join
    end
    return result
  end
  []
end
