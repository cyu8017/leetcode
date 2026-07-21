
# @param {Integer} n
# @return {Integer}
def reinitialize_permutation(n)
  perm = (0...n).to_a
  target = perm.dup
  operations = 0

  loop do
    new_perm = Array.new(n)
    n.times do |i|
      if i.even?
        new_perm[i] = perm[i / 2]
      else
        new_perm[i] = perm[n / 2 + (i - 1) / 2]
      end
    end
    perm = new_perm
    operations += 1
    return operations if perm == target
  end
end
