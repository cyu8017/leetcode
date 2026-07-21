
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def find_the_winner(n, k)
  pos = 0
  (2..n).each { |size| pos = (pos + k) % size }
  pos + 1
end
