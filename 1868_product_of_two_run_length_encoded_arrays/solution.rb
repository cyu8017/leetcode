# LeetCode 1868 - Product of Two Run-Length Encoded Arrays
# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

# @param {Integer[][]} encoded1
# @param {Integer[][]} encoded2
# @return {Integer[][]}
def find_r_l_e_array(encoded1, encoded2)
  result = []
  i = 0
  j = 0
  rem1 = encoded1[0][1]
  rem2 = encoded2[0][1]

  while i < encoded1.length
    take = [rem1, rem2].min
    value = encoded1[i][0] * encoded2[j][0]
    if !result.empty? && result[-1][0] == value
      result[-1][1] += take
    else
      result << [value, take]
    end

    rem1 -= take
    rem2 -= take
    if rem1 == 0
      i += 1
      rem1 = encoded1[i][1] if i < encoded1.length
    end
    if rem2 == 0
      j += 1
      rem2 = encoded2[j][1] if j < encoded2.length
    end
  end

  result
end
