
# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer}
def get_x_o_r_sum(arr1, arr2)
  xor1 = arr1.reduce(0, :^)
  xor2 = arr2.reduce(0, :^)
  xor1 & xor2
end
