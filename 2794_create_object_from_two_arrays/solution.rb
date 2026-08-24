# LeetCode 2794 - Create Object from Two Arrays
# https://leetcode.com/problems/create-object-from-two-arrays/

# @param {Object[]} keys_arr
# @param {Object[]} values_arr
# @return {Hash}
def create_object(keys_arr, values_arr)
  output = {}
  n = [keys_arr.length, values_arr.length].min
  (0...n).each do |i|
    key = keys_arr[i]
    key = if key == true
            "true"
          elsif key == false
            "false"
          else
            key.to_s
          end
    output[key] = values_arr[i] unless output.key?(key)
  end
  output
end
